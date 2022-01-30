from app import db,app

class User(db.model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    user_phone = db.Column(db.String(128), index=True, unique=True)
    user_address = db.relationship('Address', backref='user', lazy=True)

class Address(db.Model):
    address_id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(1024), index=True)
    email = db.Column(db.String(120), nullable=False)
    person_phone = db.Column(db.String(128), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),
        nullable=False)