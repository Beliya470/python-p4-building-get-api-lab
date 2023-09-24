from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    baked_goods = db.relationship('BakedGood', backref='bakery', lazy=True)
    serialize_only = ('id', 'name')  # Only serialize these fields
    
class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'), nullable=False)
    serialize_only = ('id', 'name', 'price', 'bakery_id')  # Only serialize these fields
