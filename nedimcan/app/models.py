from app import app,db, datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    surname = db.Column(db.String(length=50), unique=True, nullable=False)
    username = db.Column(db.String(length=50), nullable=False)
    email_address = db.Column(db.String(length=60), unique=True, nullable=False)
    password = db.Column(db.String(length=60), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_name = db.Column(db.String(length=50), unique=True, nullable=False)
