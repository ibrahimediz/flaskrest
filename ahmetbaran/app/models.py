from app import app, db

class Musteri:
    def __init__(self, isim:str, yas:int, mail:str, adres:str) -> None:
        self.isim = isim
        self.yas = yas
        self.mail = mail
        self.adres = adres