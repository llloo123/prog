# src/db/db_manager.py

import psycopg2

def create_tables():
    conn = psycopg2.connect(
        dbname="your_db",
        user="your_user",
        password="your_password",
        host="localhost"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            price DECIMAL,
            category VARCHAR(255)
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255),
            product_id INTEGER REFERENCES products(id)
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

    # src/db/db_manager.py (продолжение)

def insert_data(products, users):
    conn = psycopg2.connect(
        dbname="your_db",
        user="your_user",
        password="your_password",
        host="localhost"
    )
    cur = conn.cursor()

    for product in products:
        cur.execute("""
            INSERT INTO products (name, price, category) 
            VALUES (%(name)s, %(price)s, %(category)s)
        """, {
            'name': product[0],
            'price': product[1],
            'category': product[2]
        })

    for user in users:
        cur.execute("""
            INSERT INTO users (username, product_id) 
            SELECT %(username)s, id FROM products WHERE name = %(product_name)s
        """, {
            'username': user,
            'product_name': product[0]
        })

    conn.commit()
    cur.close()
    conn.close()