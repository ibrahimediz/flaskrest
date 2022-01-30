from app import app,db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.String(32), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    address = db.relationship('Address', backref='customer' lazy='dynamic')

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cust_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    city = db.Column(db.String(64), index=True)
    neighborhood = db.Column(db.String(64), index=True)
