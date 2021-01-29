"""Create database models to represent tables."""
from books_app import db
from sqlalchemy.orm import backref
import enum

class Audience(enum.Enum):
    CHILDREN = 1
    YOUNG_ADULT = 2
    ADULT = 3
    ALL = 4

class Book(db.Model):
    """Book model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    publish_date = db.Column(db.Date)

    # The author - Who wrote it?
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author = db.relationship('Author', back_populates='books')
    
    # The audience - Who is this book written for?
    audience = db.Column(db.Enum(Audience), default=Audience.ALL)

    # The genres, e.g. fiction, sci-fi, fantasy
    genres = db.relationship('Genre', secondary='book_genre', back_populates='books')
    users = db.relationship('User', secondary='favorite_book', back_populates='books') #secondary? back_populates


    def __str__(self):
        return f'<Book: {self.title}> <Publish Date: {self.publish_date}> <Audience: {self.audience}> STR'

    def __repr__(self):
        return f'<Book: {self.title}> <Publish Date: {self.publish_date}> <Audience: {self.audience}> REPR'

class Author(db.Model):
    """Author model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    books = db.relationship('Book', back_populates='author')

    def __str__(self):
        return f'<Author: {self.name}>'

    def __repr__(self):
        return f'<Author: {self.name}>'

class Genre(db.Model):
    """Genre model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    books = db.relationship('Book', secondary='book_genre', back_populates='genres') #secondary? back_populates

    def __str__(self):
        return f'<Genre: {self.name}>'

    def __repr__(self):
        return f'<Genre: {self.name}>'

class User(db.Model):
    '''User Model'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    books = db.relationship('Book', secondary='favorite_book', back_populates='users')
    def __repr__(self):
      return f'<User: {self.username}> <Books: {self.books}>'

book_genre_table = db.Table('book_genre',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
)
favorite_book_table = db.Table('favorite_book',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)
