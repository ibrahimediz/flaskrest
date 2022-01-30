from app import app,db
from datetime import datetime

class Customer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(40),nullable=False)
    last_name = db.Column(db.String(40),nullable=False)
    email = db.Column(db.String,unique=True,nullable=False)
    birth_date = db.Column(db.DateTime)
    phone_number = db.Column(db.String(11),unique=True)
    accountNo_hash = db.Column(db.Integer,unique=True)
    records = db.relationship('CustomerRecords',backref='record',lazy='dynamic')


class CustomerRecords(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    rec_type = db.Column(db.Integer,nullable=False)
    rec_time = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.id'))


    