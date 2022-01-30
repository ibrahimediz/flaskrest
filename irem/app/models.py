from app import app,db
from datetime import datetime

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),index=True,unique=True)
    surname = db.Column(db.String(50),index=True,unique=True)
    email = db.Column(db.String(50),index=True,unique=True)
    addres = db.Column(db.String(150),index=True,unique=True)

    
