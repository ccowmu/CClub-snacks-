from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# define what our database user looks like.
class Product(db.Model):

    __tablename__ = "products"

    productName = db.Column('productName', db.String(100), primary_key=True)
    pType = db.Column('pType', db.String(10))
    cost = db.Column('cost', db.DECIMAL(2,2))
    amount = db.Column('amount', db.Integer())

    def __init__(self, productName, pType, cost):
        self.productName = productName
        self.pType = pType
        self.cost = cost
        self.amount += 1

    def get_productName(self):
        return unicode(self.productName)

class Member(db.Model):
    memberID = db.Column(db.String(45), primary_key=True)
    nick = db.Column(db.String(45), index=True, unique=True)
    tab = db.Column(db.DECIMAL())
    username = nick

    def __repr__(self):
        return '{}'.format(self.username)

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True

    def get_id(self):
        return self.memberID

class Transactions(db.Model):
    transactionID = db.Column(db.Integer, primary_key=True)
    memberID = db.Column(db.String(45), index=True, unique=True)
    productName = db.Column(db.String(45), index=True, unique=True)
    quantity = db.Column(db.Integer)
    purchaseDate = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Transactions {}>'.format(self.username)
