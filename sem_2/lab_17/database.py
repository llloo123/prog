from models import Base, Publisher, Author, Book, book_author
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_database():
    engine = create_engine('sqlite:///books.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Добавление тестовых данных
    pub1 = Publisher(name="Эксмо")
    pub2 = Publisher(name="АСТ")
    pub3 = Publisher(name="Питер")

    auth1 = Author(name="Достоевский Ф.М.")
    auth2 = Author(name="Толстой Л.Н.")
    auth3 = Author(name="Стругацкий А.")
    auth4 = Author(name="Стругацкий Б.")

    book1 = Book(title="Преступление и наказание", year=1866, publisher=pub1)
    book1.authors = [auth1]

    book2 = Book(title="Война и мир", year=1869, publisher=pub2)
    book2.authors = [auth2]

    book3 = Book(title="Пикник на обочине", year=1972, publisher=pub3)
    book3.authors = [auth3, auth4]

    session.add_all([pub1, pub2, pub3, auth1, auth2, auth3, auth4, book1, book2, book3])
    session.commit()
    print("База данных успешно создана и заполнена!")

if __name__ == "__main__":
    create_database()