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

    def to_dict(self):
        data={
            id = self.id,
            first_name = self.first_name,
            last_name = self.last_name,
            email = self.email,
            birth_date = self.birth_date,
            phone_number = self.phone_number,
            accountNo_hash = self.accountNo_hash,
        }
        return data

    def from_dict(self,data):
        for field in ["first_name","last_name","email","birth_date","phone_number","accountNo_hash"]:
            if field in data:
                setattr(self,field,data[field])

    def __repr__(self):
        return '<Customer {} {}>'.format(self.first_name,self.last_name) 

class CustomerRecords(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    rec_type = db.Column(db.Integer,nullable=False)
    rec_time = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.id'))

    def __repr__(self):
        return '<Record {} {}>'.format(self.id,self.customer_id)