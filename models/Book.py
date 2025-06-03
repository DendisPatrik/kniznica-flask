from app import db


class Book(db.Model):
    __tablename__ = 'books'

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))
    isbn = db.Column(db.String(13))
    publication_year = db.Column(db.Integer)
    copies = db.Column(db.Integer, default=1)

    author = db.relationship("Author", back_populates="books")
    genre = db.relationship("Genre", back_populates="books")