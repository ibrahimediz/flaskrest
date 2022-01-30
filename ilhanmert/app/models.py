from app import app, db

class User():
    id = db.Column(db.Integer, primary_key=True)
    kullanici_adi = db.Column(db.String(64), unique=True)
    eposta = db.Column(db.String(120), unique=True)