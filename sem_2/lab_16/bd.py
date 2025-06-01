import sqlite3
from parser import get_books

def create_tables(conn):
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            rating INTEGER,
            FOREIGN KEY(book_id) REFERENCES books(id)
        )
    """)
    conn.commit()

def insert_data(conn, books):
    c = conn.cursor()
    for book in books:
        c.execute("INSERT INTO books (title, price) VALUES (:title, :price)", {"title": book["title"], "price": book["price"]})
        book_id = c.lastrowid
        c.execute("INSERT INTO ratings (book_id, rating) VALUES (:book_id, :rating)", {"book_id": book_id, "rating": book["rating"]})
    conn.commit()

def main():
    books = get_books()
    print(f"Найдено книг: {len(books)}")

    conn = sqlite3.connect("books.db")
    create_tables(conn)
    insert_data(conn, books)
    print("Данные успешно сохранены в books.db")
    conn.close()

if __name__ == "__main__":
    main()