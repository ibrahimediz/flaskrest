from app import app,db, datetime

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    surname = db.Column(db.String(length=50), unique=True, nullable=False)
    birt_date = db.Column(db.DateTime, nullable=False)
    username = db.Column(db.String(length=50), nullable=False)
        phone_number = db.Column(db.String(11),unique=True,nullable=False)
    email_address = db.Column(db.String(length=60), unique=True, nullable=False)
    password = db.Column(db.String(length=60), nullable=False)
    accountNo_hash = db.Column(db.Integer,unique=True,nullable=False)