from app import app
from sqlalchemy import Column, Integer, String
class Musteri(Base):

    id = Column(Integer, primary_key=True)
    name = Column(String)
    full_name = Column(String)
    nickname = Column(String)
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
           self.name, self.fullname, self.nickname)