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
