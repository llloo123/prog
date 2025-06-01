def top_artists_by_paintings_count(n):
    conn = sqlite3.connect('expensive_paintings.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT a.name, COUNT(p.painting_id) as painting_count
    FROM artists a
    JOIN paintings p ON a.artist_id = p.artist_id
    GROUP BY a.name
    ORDER BY painting_count DESC
    LIMIT ?
    ''', (n,))
    
    results = cursor.fetchall()
    conn.close()
    return results

def top_artists_by_paintings_price(n):
    conn = sqlite3.connect('expensive_paintings.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT a.name, SUM(p.price) as total_price
    FROM artists a
    JOIN paintings p ON a.artist_id = p.artist_id
    GROUP BY a.name
    ORDER BY total_price DESC
    LIMIT ?
    ''', (n,))
    
    results = cursor.fetchall()
    conn.close()
    return results


def most_expensive_paintings_by_year():
    conn = sqlite3.connect('expensive_paintings.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT p.creation_year, p.title, a.name, p.price
    FROM paintings p
    JOIN artists a ON p.artist_id = a.artist_id
    WHERE (p.creation_year, p.price) IN (
        SELECT creation_year, MAX(price)
        FROM paintings
        GROUP BY creation_year
    )
    ORDER BY p.creation_year DESC
    ''')
    
    results = cursor.fetchall()
    conn.close()
    return results

def total_price_top_n_paintings(n):
    conn = sqlite3.connect('expensive_paintings.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT SUM(price) as total_price
    FROM (
        SELECT price
        FROM paintings
        ORDER BY price DESC
        LIMIT ?
    )
    ''', (n,))
    
    result = cursor.fetchone()[0]
    conn.close()
    return result