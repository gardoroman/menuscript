from app import db
from sqlalchemy.dialects.postgresql import JSON

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(64), index=True, unique=True)
    address = db.Column(db.String(200), index=True, unique=True)
    phone = db.Column(db.String(15))
    cuisine_type = db.Column(db.String(50))
    opening_time = db.Column(db.String(15))
    closing_time = db.Column(db.String(15))
    menus = db.relationship('Menu', backref='store', lazy='dynamic')

    def __repr__(self):
        return '<Store %r>' % (self.store_name)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80))
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    items = db.relationship('Item', backref='menu', lazy='dynamic')

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(80))
    section = db.Column(db.String(30))
    price = db.Column(db.String(15))
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))
