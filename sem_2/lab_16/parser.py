import sqlite3
from time import sleep
from random import uniform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException, 
                                      TimeoutException,
                                      StaleElementReferenceException)
from pypika import Query, Table, Field, functions as fn, Order

class BookParser:
    def __init__(self):
        # Инициализация драйвера для Safari на M1
        self.setup_driver()
        # Подключение к БД
        self.conn = sqlite3.connect('labirint_books_v2.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        # Создание таблиц
        self.create_tables()
        
    def setup_driver(self):
        """Настройка WebDriver для Safari на Mac M1"""
        safari_options = webdriver.safari.options.Options()
        safari_options.headless = True
        self.driver = webdriver.Safari(options=safari_options)
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
    
    def create_tables(self):
        """Создание улучшенной структуры БД"""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            author_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            bio TEXT,
            rating REAL DEFAULT 0.0,
            books_count INTEGER DEFAULT 0
        )''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS genres (
            genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price REAL,
            original_price REAL,
            discount INTEGER DEFAULT 0,
            rating REAL DEFAULT 0.0,
            reviews_count INTEGER DEFAULT 0,
            year INTEGER,
            pages INTEGER,
            cover_type TEXT,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(author_id)
        )''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS book_genres (
            book_id INTEGER,
            genre_id INTEGER,
            PRIMARY KEY (book_id, genre_id),
            FOREIGN KEY (book_id) REFERENCES books(book_id),
            FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
        )''')
        
        self.conn.commit()
    
    def random_delay(self):
        """Случайная задержка между запросами"""
        sleep(uniform(1.5, 3.5))
    
    def parse_book_page(self, url):
        """Парсинг детальной страницы книги"""
        try:
            self.driver.get(url)
            self.random_delay()
            
            book_data = {
                'title': self.get_text_or_default('h1'),
                'price': self.get_price('div.buying-price-val-number'),
                'original_price': self.get_price('div.buying-priceold-val-number'),
                'rating': self.get_float('div.left div.rating'),
                'reviews_count': self.get_int('div.left a.reviews-link span'),
                'year': self.get_int('div.publisher span:nth-child(2)'),
                'pages': self.get_int('div.publisher span:nth-child(4)'),
                'cover_type': self.get_text_or_default('div.publisher span:nth-child(6)')
            }
            
            # Расчет скидки
            if book_data['original_price'] and book_data['price']:
                book_data['discount'] = int(100 - (book_data['price'] / book_data['original_price'] * 100))
            
            return book_data
        except Exception as e:
            print(f"Ошибка при парсинге страницы книги {url}: {e}")
            return None
    
    def get_text_or_default(self, selector, default=""):
        """Безопасное получение текста"""
        try:
            return self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
            ).text.strip()
        except:
            return default
    
    def get_price(self, selector):
        """Парсинг цены"""
        try:
            price_text = self.get_text_or_default(selector)
            return float(price_text.replace(' ', '').replace('₽', ''))
        except:
            return None
    
    def get_float(self, selector):
        """Парсинг чисел с плавающей точкой"""
        try:
            return float(self.get_text_or_default(selector))
        except:
            return 0.0
    
    def get_int(self, selector):
        """Парсинг целых чисел"""
        try:
            text = self.get_text_or_default(selector)
            return int(''.join(filter(str.isdigit, text)))
        except:
            return 0
    
    def save_author(self, name):
        """Сохранение автора с проверкой на существование"""
        self.cursor.execute(
            "INSERT OR IGNORE INTO authors (name) VALUES (?)", 
            (name.strip(),)
        )
        self.conn.commit()
        return self.cursor.lastrowid or self.get_author_id(name)
    
    def get_author_id(self, name):
        """Получение ID автора"""
        self.cursor.execute(
            "SELECT author_id FROM authors WHERE name = ?", 
            (name.strip(),)
        )
        result = self.cursor.fetchone()
        return result[0] if result else None
    
    def save_genre(self, name):
        """Сохранение жанра"""
        self.cursor.execute(
            "INSERT OR IGNORE INTO genres (name) VALUES (?)", 
            (name.strip(),)
        )
        self.conn.commit()
        return self.cursor.lastrowid or self.get_genre_id(name)
    
    def get_genre_id(self, name):
        """Получение ID жанра"""
        self.cursor.execute(
            "SELECT genre_id FROM genres WHERE name = ?", 
            (name.strip(),)
        )
        result = self.cursor.fetchone()
        return result[0] if result else None
    
    def save_book(self, book_data, author_name, genres=[]):
        """Сохранение книги и связанных данных"""
        try:
            author_id = self.save_author(author_name)
            
            self.cursor.execute('''
            INSERT INTO books (
                title, price, original_price, discount, 
                rating, reviews_count, year, pages, cover_type, author_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                book_data['title'], book_data['price'], book_data['original_price'],
                book_data.get('discount', 0), book_data['rating'], book_data['reviews_count'],
                book_data['year'], book_data['pages'], book_data['cover_type'], author_id
            ))
            book_id = self.cursor.lastrowid
            
            # Сохранение жанров
            for genre_name in genres:
                genre_id = self.save_genre(genre_name)
                self.cursor.execute(
                    "INSERT OR IGNORE INTO book_genres VALUES (?, ?)",
                    (book_id, genre_id)
                )
            
            self.conn.commit()
            return book_id
        except Exception as e:
            print(f"Ошибка при сохранении книги: {e}")
            self.conn.rollback()
            return None
    
    def parse_books_from_page(self, url):
        """Парсинг списка книг со страницы"""
        try:
            self.driver.get(url)
            self.random_delay()
            
            # Принимаем куки, если есть
            try:
                cookie_btn = self.driver.find_element(By.CSS_SELECTOR, "button.cookie-policy__button")
                cookie_btn.click()
                self.random_delay()
            except:
                pass
            
            books = []
            items = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-cover"))
            )
            
            for item in items[:5]:  # Ограничимся 5 книгами для примера
                try:
                    # Прокрутка к элементу
                    self.driver.execute_script("arguments[0].scrollIntoView();", item)
                    self.random_delay()
                    
                    title = item.find_element(By.CSS_SELECTOR, "a.product-title-link").text
                    author = item.find_element(By.CSS_SELECTOR, "div.product-author").text
                    book_url = item.find_element(By.CSS_SELECTOR, "a.product-title-link").get_attribute("href")
                    
                    # Парсинг детальной страницы
                    book_data = self.parse_book_page(book_url)
                    if not book_data:
                        continue
                    
                    # Получение жанров (если есть)
                    genres = []
                    try:
                        genre_elements = item.find_elements(By.CSS_SELECTOR, "div.genre a")
                        genres = [g.text for g in genre_elements if g.text]
                    except:
                        pass
                    
                    # Сохранение книги
                    book_id = self.save_book(book_data, author, genres)
                    if book_id:
                        books.append(book_id)
                        print(f"Сохранена книга: {title} (ID: {book_id})")
                    
                except (NoSuchElementException, StaleElementReferenceException) as e:
                    print(f"Пропуск книги из-за ошибки: {e}")
                    continue
            
            return books
        except Exception as e:
            print(f"Ошибка при парсинге страницы: {e}")
            return []
    
    def generate_queries(self):
        """Генерация SQL-запросов с использованием PyPika"""
        books = Table('books')
        authors = Table('authors')
        genres = Table('genres')
        book_genres = Table('book_genres')
        
        # 1. JOIN: Книги с авторами и жанрами
        query1 = (Query.from_(books)
                 .join(authors).on(books.author_id == authors.author_id)
                 .left_join(book_genres).on(books.book_id == book_genres.book_id)
                 .left_join(genres).on(book_genres.genre_id == genres.genre_id)
                 .select(books.title, authors.name.as_('author'), 
                         fn.GroupConcat(genres.name).as_('genres'))
                 .groupby(books.book_id)
                )
        
        # 2. JOIN: Авторы с количеством книг и средним рейтингом
        query2 = (Query.from_(authors)
                 .left_join(books).on(authors.author_id == books.author_id)
                 .select(authors.name, 
                         fn.Count(books.book_id).as_('total_books'),
                         fn.Avg(books.rating).as_('avg_rating'))
                 .groupby(authors.author_id)
                 .orderby('total_books', order=Order.desc)
                )
        
        # 3. Статистика по жанрам
        query3 = (Query.from_(genres)
                 .left_join(book_genres).on(genres.genre_id == book_genres.genre_id)
                 .left_join(books).on(book_genres.book_id == books.book_id)
                 .select(genres.name,
                         fn.Count(books.book_id).as_('books_count'),
                         fn.Avg(books.price).as_('avg_price'),
                         fn.Max(books.discount).as_('max_discount'))
                 .groupby(genres.genre_id)
                 .having(fn.Count(books.book_id) > 0)
                )
        
        # 4. Топ-10 книг по рейтингу
        query4 = (Query.from_(books)
                 .join(authors).on(books.author_id == authors.author_id)
                 .select(books.title, authors.name.as_('author'), 
                         books.rating, books.reviews_count)
                 .orderby(books.rating, order=Order.desc)
                 .limit(10)
                )
        
        # 5. Анализ скидок
        query5 = (Query.from_(books)
                 .select(fn.Avg(books.discount).as_('avg_discount'),
                         fn.Max(books.discount).as_('max_discount'),
                         fn.Sum(case().when(books.discount > 30, 1).else_(0)).as_('big_discounts_count'))
                 .where(books.discount > 0)
                )
        
        queries = {
            "Книги с авторами и жанрами": query1,
            "Авторы с количеством книг": query2,
            "Статистика по жанрам": query3,
            "Топ-10 книг по рейтингу": query4,
            "Анализ скидок": query5
        }
        
        # Выполнение и вывод результатов
        for name, query in queries.items():
            sql = query.get_sql()
            print(f"\n{name}:\n{sql}")
            try:
                self.cursor.execute(sql)
                results = self.cursor.fetchall()
                print(f"Результаты ({len(results)} записей):")
                for row in results[:5]:  # Показываем первые 5 результатов
                    print(row)
            except Exception as e:
                print(f"Ошибка выполнения запроса: {e}")
    
    def close(self):
        """Завершение работы"""
        self.driver.quit()
        self.conn.close()
        print("Парсер завершил работу")

# Запуск парсера
if __name__ == "__main__":
    parser = BookParser()
    try:
        # Парсинг нескольких страниц (можно добавить больше URL)
        urls = [
            "https://www.labirint.ru/genres/2308/",  # Художественная литература
            "https://www.labirint.ru/genres/1852/",  # Фантастика
            "https://www.labirint.ru/genres/1858/"   # Детективы
        ]
        
        for url in urls:
            print(f"\nПарсинг страницы: {url}")
            parser.parse_books_from_page(url)
        
        # Генерация и выполнение запросов
        print("\nГенерация аналитических запросов:")
        parser.generate_queries()
        
    except Exception as e:
        print(f"Критическая ошибка: {e}")
    finally:
        parser.close()
        