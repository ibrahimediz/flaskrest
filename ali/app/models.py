from app import db,app
from datetime import datetime

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    user_phone = db.Column(db.String(128), index=True, unique=True)
    records = db.relationship('CustomerRecord', backref='record', lazy='dynamic')
#     user_address = db.relationship('Address', backref='user', lazy=True)

    def to_dict(self):
        data = {
            'user_id':self.user_id,  
            'username':self.username,
            'email':self.email,
            'user_phone':self.user_phone        }
        return data
    
    def from_dict(self,data):
        for field in ["user_id","username","email","user_phone","records"]:
            if field in data:
                setattr(self,field,data[field])        
            

    def __repr__(self):
        return '<User {} {}>'.format(self.username,self.email,self.user_phone)

# class Address(db.Model):
#     address_id = db.Column(db.Integer, primary_key=True)
#     address = db.Column(db.String(1024), index=True)
#     email = db.Column(db.String(120), nullable=False)
#     person_phone = db.Column(db.String(128), nullable=False)
#     person_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),
#         nullable=False)

class CustomerRecord(db.Model):
    record_id = db.Column(db.Integer, primary_key=True)
    rec_type = db.Column(db.Integer, nullable=False)
    rec_time = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __repr__(self):
         return '<Record {} {}>'.format(self.record_id, self.customer_id)

