from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)


# publishing_house: id, name, rating (default 5)
class PublishingHouses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, default=5)


# books: id, title, author, year, price, publishing_house_id
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String,)
    author = db.Column(db.String,)
    year = db.Column(db.String,)
    price = db.Column(db.Integer,)
    publishing_house_id = db.Column(db.Integer, db.ForeignKey('publishing_houses.id'), nullable=False)
    publishing_house = db.relationship('PublishingHouses')


# purchases: id, user_id, book_id, date
class Purchases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users')
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    book = db.relationship('Books')
    date = db.Column(db.TIMESTAMP)
