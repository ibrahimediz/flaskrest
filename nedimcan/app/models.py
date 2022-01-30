from app import app,db, datetime

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    surname = db.Column(db.String(length=50), unique=True, nullable=False)
    birth_date = db.Column(db.DateTime)
    username = db.Column(db.String(length=50), nullable=False)
    phone_number = db.Column(db.String(11),unique=True,nullable=False)
    account_no_hash = db.Column(db.Integer,unique=True,nullable=False)
    record = db.relationship('CustomerRecords', backref='record', lazy='dynamic')

    def to_dict(self):
        data = {
            "id":self.id,
            "name":self.name,
            "surname":self.surname,
            #"email":self.email
            "username":self.username,
            "birth_date":self.birth_date,
            "phone_number":self.phone_number,
            "account_no_hash":self.account_no_hash
        }

        return data

    def from_dict(self,data):
        for field in ['name','surname','username','birth_date','phone_number']:
            if field in data:
                setattr(self,field,data[field])

    @staticmethod
    def to_collection_dict(query):
        data = { customer.id : customer.to_dict() for customer in query}
        retun data

    def __repr__(self):
        return "<Customer {} {}>".format(self.name,self.surname)

class CustomerRecords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rec_type = db.Column(db.Integer, nullable=False)
    rec_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def __repr__(self):
        return "<Record {} {}>".format(self.id,self.customer_id)