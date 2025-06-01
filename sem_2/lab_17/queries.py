from models import Base, Publisher, Author, Book
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///books.db')
Session = sessionmaker(bind=engine)
session = Session()

def run_queries():
    print("\n1. Все книги с авторами и издательствами:")
    books = session.query(Book).all()
    for book in books:
        authors = ", ".join([author.name for author in book.authors])
        print(f"{book.title} ({book.year}) - {authors}. Издательство: {book.publisher.name}")

    print("\n2. Книги Стругацкого А.:")
    author_books = session.query(Book).join(Book.authors).filter(Author.name == "Стругацкий А.").all()
    for book in author_books:
        print(f"- {book.title}")

    print("\n3. Статистика по издательствам:")
    publisher_stats = session.query(
        Publisher.name,
        func.count(Book.id).label('book_count')
    ).join(Publisher.books).group_by(Publisher.name).all()
    for pub in publisher_stats:
        print(f"{pub.name} - {pub.book_count} книг")

if __name__ == "__main__":
    run_queries()