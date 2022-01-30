from app import app, db
from datetime import datetime

class Customer(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(64),nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    address = db.Column(db.String(360),nullable=False)
    records = db.relationship('CustomerRecords',backref='ref',lazy='dynamic')

    def __repr__(self):

        return '<Customer {} {}'.format(self.first_name,self.last_name)
class CustomerRecords(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    rec_type = db.Column(db.Integer,nullable=False)
    rect_time = db.Column(db.DateTime,nullable=False,default=datetime.now())
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.id'))


    def __repr__(self):

        return '<Record {} {}'.format(self.id,self.customer_id)