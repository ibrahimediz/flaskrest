from app import app,db

class User(db.model):
    user_id = db.Column(db.Integer, primary_key = true)
    account_no_hash = db.Column(db.String(128))
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    name = db.Column(db.String(64), index=True, nullable=False)
    last_name = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    phone_num = db.Column(db.String(64), index=True, nullable=False)
