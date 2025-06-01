import requests
from bs4 import BeautifulSoup
import re
import sqlite3
from datetime import datetime

def parse_expensive_paintings():
    url = "https://en.wikipedia.org/wiki/List_of_most_expensive_paintings"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    paintings = []
    artists = set()
    locations = set()
    
    # Находим таблицу с картинами
    tables = soup.find_all('table', {'class': 'wikitable'})
    main_table = tables[0]  # Первая таблица содержит нужные данные
    
    for row in main_table.find_all('tr')[1:]:  # Пропускаем заголовок
        cols = row.find_all('td')
        if len(cols) >= 5:
            # Парсим данные о картине
            title = cols[0].get_text(strip=True)
            artist = cols[1].get_text(strip=True)
            price_str = cols[2].get_text(strip=True)
            date_str = cols[3].get_text(strip=True)
            location = cols[4].get_text(strip=True)
            
            # Обрабатываем цену
            price_match = re.search(r'\$(\d+\.?\d*) million', price_str)
            if price_match:
                price = float(price_match.group(1)) * 1000000
            else:
                continue  # Пропускаем если не удалось распарсить цену
                
            # Обрабатываем дату
            try:
                date = datetime.strptime(date_str, '%d %B %Y').strftime('%Y-%m-%d')
                year = date_str.split()[-1]
            except:
                year = date_str.split()[-1]  # Берем только год если не удается распарсить дату
                
            # Добавляем художника
            artists.add((artist, '', '', '', ''))  # Остальные данные можно заполнить дополнительным парсингом
            
            # Добавляем место продажи
            locations.add((location, '', '', ''))
            
            # Добавляем картину
            paintings.append({
                'title': title,
                'artist': artist,
                'price': price,
                'year': year,
                'location': location,
                'dimensions': '',
                'medium': ''
            })
    
    return {
        'paintings': paintings,
        'artists': list(artists),
        'locations': list(locations)
    }

def create_database():
    conn = sqlite3.connect('expensive_paintings.db')
    cursor = conn.cursor()
    
    # Создаем таблицу художников
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS artists (
        artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year INTEGER,
        death_year INTEGER,
        nationality TEXT,
        style TEXT
    )
    ''')
    
    # Создаем таблицу мест продаж
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS locations (
        location_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT,
        country TEXT,
        auction_house TEXT
    )
    ''')
    
    # Создаем таблицу картин
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS paintings (
        painting_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        artist_id INTEGER,
        creation_year INTEGER,
        price REAL,
        location_id INTEGER,
        dimensions TEXT,
        medium TEXT,
        FOREIGN KEY (artist_id) REFERENCES artists (artist_id),
        FOREIGN KEY (location_id) REFERENCES locations (location_id)
    )
    ''')
    
    # Получаем данные с помощью парсера
    data = parse_expensive_paintings()
    
    # Заполняем таблицу художников
    for artist in data['artists']:
        cursor.execute('''
        INSERT INTO artists (name, birth_year, death_year, nationality, style)
        VALUES (?, ?, ?, ?, ?)
        ''', artist)
    
    # Заполняем таблицу мест продаж
    for location in data['locations']:
        cursor.execute('''
        INSERT INTO locations (name, city, country, auction_house)
        VALUES (?, ?, ?, ?)
        ''', location)
    
    # Заполняем таблицу картин
    for painting in data['paintings']:
        # Получаем artist_id
        cursor.execute('SELECT artist_id FROM artists WHERE name = ?', (painting['artist'],))
        artist_id = cursor.fetchone()[0]
        
        # Получаем location_id
        cursor.execute('SELECT location_id FROM locations WHERE name = ?', (painting['location'],))
        location_id = cursor.fetchone()[0]
        
        cursor.execute('''
        INSERT INTO paintings (title, artist_id, creation_year, price, location_id, dimensions, medium)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            painting['title'],
            artist_id,
            painting['year'],
            painting['price'],
            location_id,
            painting['dimensions'],
            painting['medium']
        ))
    
    conn.commit()
    conn.close()

create_database()