from app import app, db

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(128), index=True, unique=True)
    age = db.Column(db.Integer, index=True)
    password_hash = db.Column(db.String(128))
    phone_number = db.Column(db.String(11), unique=True, index=True)