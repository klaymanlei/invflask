#coding: utf-8

from mysql_tools import db

class User(db.Model):

   __tablename__ = 't_user'

   id = db.Column(db.Integer, primary_key = True, autoincrement = True)
   username = db.Column(db.String(64), nullable = False, unique=True)
   password = db.Column(db.String(64), nullable = False)
   email = db.Column(db.String(64), nullable = False, unique=True)
   role = db.Column(db.String(20), nullable = False, default = 'user')

   def __repr__(self):
       return '<%s: (%r, %s)>' % (self.__class__.__name__, self.username, self.role)

class Transaction(db.Model):
    __tablename__ = 't_transaction'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    dt = db.Column(db.Date, index = True)
    code = db.Column(db.String(50))
    operation = db.Column(db.String(50))
    portfolio = db.Column(db.String(50))
    sec_type = db.Column(db.String(50))
    quantity = db.Column(db.Float)
    price = db.Column(db.Float)
    tax = db.Column(db.Float)
    other_charges = db.Column(db.Float)
    amount = db.Column(db.Float)

    def __repr__(self):
        return '<%s: %d, %s, %s>' % (self.__class__.__name__, self.id, self.dt, self.code)
