from app import app, db


class Customer(db.Model):

    id = db.Column(db.Integer,primary_key=True,nullable=False)
    first_name = db.Column(db.String(64), index=True,nullable=False)
    last_name = db.Column(db.String(64), index=True,nullable=False)
    email = db.Column(dbString(120),index=True,unique=True,nullable=False)
    address = db.Column(dbString(360),index=True,nullable=False)