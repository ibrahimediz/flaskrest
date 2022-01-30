from app import app,db

class Customer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String,nullable=False)
    last_name = db.Column(db.String,nullable=False)
    email = db.Column(db.String,unique=True,nullable=False)
    birth_date = db.Column(db.DateTime,nullable=False)
    phone_number = db.Column(db.String(11),unique=True,nullable=False)
    accountNo_hash = db.Column(db.Integer,unique=True,nullable=False)
