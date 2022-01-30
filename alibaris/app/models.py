from app import app,db
from datetime import datetime

class Customer(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    account_no_hash = db.Column(db.String(128),unique=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    name = db.Column(db.String(64), index=True, nullable=False)
    last_name = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    phone_num = db.Column(db.String(64))
    records = db.relationship("CustomerRecords", backref = "record", lazy = "dynamic")

    def __repr__(self):
        return "<Customer {} {}>".format(self.name, self.last_name)
    
    def to_dict(self):
        data = {
            'id':self.user_id,
            'username':self.username,
            'name':self.name,
            'last_name':self.last_name,
            'email': self.email,
        }

        return data
    
    def from_dict(self, data):
        for field in ['username','name','last_name','email']:
            if field in data:
                setattr(self, field, data[field])
    
    def to_collection_dict(self):
        

class CustomerRecords(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rec_type = db.Column(db.Integer, nullable = False)
    rec_time = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.user_id'))

    def __repr__(self):
        return "<Record {} {}>".format(self.id, self.customer_id)
