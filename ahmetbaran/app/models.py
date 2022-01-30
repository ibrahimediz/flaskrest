from app import app, db
from datetime import datetime

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(128), unique=True)
    age = db.Column(db.Integer)
    password_hash = db.Column(db.String(128))
    phone_number = db.Column(db.String(11), unique=True)
    account_no_hast = db.Column(db.String(128), unique=True)

    records = db.relationship('CustomerRecords', backref='record', lazy='dynamic')

    def to_dict(self) -> dict:
        data = {
            'customer_id': self.customer_id,
            'nickname': self.nickname,
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'password_hash': self.password_hash,
            'phone_number': self.phone_number,
            'account_no_hast': self.account_no_hast
        }
        return data
    
    def from_dict(self, data:dict):
        for field in ['nickname', 'name' 'email', 'age', 'password_hash', 'phone_number', 'account_no_hast']:
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return '<Customer {}'.format(self.name)

class CustomerRecords(db.Model):
    record_id = db.Column(db.Integer, primary_key=True)
    rec_type = db.Column(db.Integer)
    rec_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))

    def __repr__(self):
        return '<Record {} {}'.format(self.record_id, self.customer_id)