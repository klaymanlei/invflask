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

class Hist_price(db.Model):
    __tablename__ = 't_hist_price'
    __table_args__ = (db.UniqueConstraint('dt', 'code', name='idx_dt_code_unique'),)
                      #db.Index('idx', 'user_id', 'insert_time'),)

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    dt = db.Column(db.Date, index = True)
    code = db.Column(db.String(50))
    price = db.Column(db.Float)

    def __repr__(self):
        return '<%s: %s, %s, %s>' % (self.__class__.__name__, self.dt, self.code, self.price)

class Holding(db.Model):
    __tablename__ = 't_holding'
    __table_args__ = (db.UniqueConstraint('dt', 'portfolio', 'code', name='idx_dt_portfolio_code_unique'),)
                      #db.Index('idx', 'user_id', 'insert_time'),)

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    dt = db.Column(db.Date, index = True)
    portfolio = db.Column(db.String(50))
    code = db.Column(db.String(50))
    sec_type = db.Column(db.String(50))
    quantity = db.Column(db.Float)
    amount = db.Column(db.Float)

    def __repr__(self):
        return '<%s: %s, %s, %s, %f>' % (self.__class__.__name__, self.dt, self.portfolio, self.code, self.amount)

class Asset(db.Model):
    __tablename__ = 't_asset'
    __table_args__ = (db.UniqueConstraint('dt', 'portfolio', 'code', name='idx_dt_portfolio_code_unique'),)
                      #db.Index('idx', 'user_id', 'insert_time'),)

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    dt = db.Column(db.Date, index = True)
    portfolio = db.Column(db.String(50))
    code = db.Column(db.String(50))
    sec_type = db.Column(db.String(50))
    quantity = db.Column(db.Float)
    amount = db.Column(db.Float)

    def __repr__(self):
        return '<%s: %s, %s, %s, %f>' % (self.__class__.__name__, self.dt, self.portfolio, self.code, self.amount)

def tostr_holding(holding):
    return (holding.dt.strftime('%Y-%m-%d'), holding.portfolio, holding.code, holding.sec_type,
            str(holding.quantity), str(holding.amount))
