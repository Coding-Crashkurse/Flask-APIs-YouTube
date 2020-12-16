from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Boolean, Integer, String, Float

def setup_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["TESTING"] = True
    db.app = app
    db.init_app(app)
    db.create_all()

db = SQLAlchemy()

class Items(db.Model):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    item = Column(String(256))
    price = Column(Float)

    def __init__(self, item, price):
        self.item = item
        self.price = price

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "item": self.item,
            "price": self.price,
        }