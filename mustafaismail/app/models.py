from app import app,db

class Customer(db.class (models.Model):

    
    id = db.Column(db.Integer, primarykey = True)
    username = db.Column(db.String(64), index = True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    address = db.Column(db.String(256), index = True)