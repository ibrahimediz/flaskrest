from app import app,db
from datetime import datetime

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.String(32), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    records = db.relationship('CustomerRecords', backref='record',lazy='dynamic')
    def __repr__(self):
        return '<Customer {} {}'.format(self.username)

class CustomerRecords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rec_type = db.Column(db.Integer,nullable=False)
    rec_time = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.id'))

    def __repr__(self):
        return '<Record {} {}>'.format(self.id,self.customer_id)