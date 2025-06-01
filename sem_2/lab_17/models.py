from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

book_author = Table(
    'book_author',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('author_id', Integer, ForeignKey('author.id'))
)

class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", back_populates="publisher")

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", secondary=book_author, back_populates="authors")

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    publisher_id = Column(Integer, ForeignKey('publisher.id'))
    publisher = relationship("Publisher", back_populates="books")
    authors = relationship("Author", secondary=book_author, back_populates="books")