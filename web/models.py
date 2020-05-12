# models.py


import datetime
from app import db


class Post(db.Model):

    __tablename__ = 'retoibm'

    id = db.Column(db.Integer, primary_key=True)
    sumando01 = db.Column(db.String, nullable=False)
    sumando02 = db.Column(db.String, nullable=False)
    resultado = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)

    def __init__(self, sumando01, sumando02, resultado):
        self.sumando01 = sumando01
        self.sumando02 = sumando02
        self.resultado = resultado
        self.date_posted = datetime.datetime.now()
