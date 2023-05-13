from app import db

class Vereniging(db.Model):
    __tablename__ = 'verenigingen'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    beer_count = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name
        self.beer_count = 0

    def add_beer(self, amount):
        self.beer_count += amount