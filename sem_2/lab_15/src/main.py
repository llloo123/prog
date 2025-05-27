# src/main.py

from src.parser.selenium_parser import get_data
from src.db.db_manager import create_tables, insert_data
from src.db.queries import get_queries

if __name__ == "__main__":
    # Создание таблиц
    create_tables()

    # Получение данных с помощью парсера
    products, users = get_data()

    # Вставка данных в таблицы
    insert_data(products, users)

    # Получение и вывод SQL-запросов
    queries = get_queries()
    for query in queries:
        print(query)