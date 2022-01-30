from app import app,db
from datetime import datetime

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),index=True,unique=True)
    surname = db.Column(db.String(50),index=True,unique=True)
    email = db.Column(db.String(50),index=True,unique=True)
    addres = db.Column(db.String(150),index=True,unique=True)
    records = db.relationship('CustomerRecords',backref='record',lazy='dynamic')

    def __repr__(self):
        return '<Customer {} {}>'.format(self.first_name,self.last_name) 

class CustomerRecords(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    rec_type = db.Column(db.Integer,nullable=False)
    rec_time = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.id'))

    def __repr__(self):
        return '<Record {} {}>'.format(self.id,self.customer_id)


