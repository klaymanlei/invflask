#coding: utf-8

from mysql_tools import db
from models import User, Transaction

def create_tables():
    db.create_all()

def add_user(username, password, email, role = 'user'):
    user = User(username = username, password = password, email = email)
    db.session.add(user)
    db.session.commit()

def fetch_user(username = '', email_like = ''):
    if (username == '' and email_like == '') or username == None or email_like == None:
        return []
    if username == '':
        return User.query.filter(User.email.like('%' + email_like + '%')).all()
    elif email_like == '':
        return User.query.filter_by(username = username).all()
    else:
        return User.query.filter(User.username == username, User.email.like('%' + email_like + '%')).all()

def fetch_transaction(start_date, end_date = '', code=''):
    if ((start_date == '' and code == '')
        or (end_date <> '' and end_date < start_date)
        or start_date == None
        or end_date == None
        or code == None):
        return []
    if end_date == '':
        end_date = start_date
    if code == '':
        return Transaction.query.filter(Transaction.dt >= start_date, Transaction.dt <= end_date).all()
    else:
        return Transaction.query.filter(Transaction.dt >= start_date, Transaction.dt <= end_date, Transaction.code == code).all()


add_user('leidayu', 'leidayu', 'leidayu@123.com', 'admin')

# query data
#user = fetch_user(email_like='123')
#transactions  = fetch_transaction('2016-03-07', '2016-03-31', '204001')
#print transactions

# modify data
#user.role = 'admin'
#db.session.add(user)
#db.session.commit()

# remove data
#db.session.delete(user)
#db.session.commit()