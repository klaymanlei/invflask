#coding: utf-8

import sys
import traceback

from mysql_tools import db
from models import *

from scripts import sqls

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

def fetch_transaction(start_date, end_date = '', code = ''):
    start_date, end_date, code = process_params(start_date, end_date, code)
    if code == '':
        return Transaction.query.filter(Transaction.dt >= start_date, Transaction.dt <= end_date).all()
    else:
        return Transaction.query.filter(Transaction.dt >= start_date, Transaction.dt <= end_date, Transaction.code == code).all()

def save_transaction(dt, code, oper, portf, sectype, quantity, price, tax, othercharge, amount):
    trans = Transaction(dt=dt, code=code, operation=oper, portfolio=portf, sec_type=sectype, quantity=quantity,
                        price=price,
                        tax=tax, other_charges=othercharge, amount=amount)
    db.session.add(trans)
    db.session.commit()

def save_all_holdings(hlds):
    db.session.add_all(hlds)
    db.session.commit()

def save_all_asset(assets):
    db.session.add_all(assets)
    db.session.commit()

def import_code_prc(path):
    file = open(path, 'r')
    data = {}
    for line in file:
        rec = line.strip().split("\t")
        data[(rec[0], rec[1])] = Hist_price(dt=rec[0], code=rec[1], price=rec[2])
    db.session.add_all(data.values())
    db.session.commit()

def fetch_holding(start_date, end_date = '', code = ''):
    start_date, end_date, code = process_params(start_date, end_date, code)
    if code == '':
        return Holding.query.filter(Holding.dt >= start_date, Holding.dt <= end_date).all()
    else:
        return Holding.query.filter(Holding.dt >= start_date, Holding.dt <= end_date, Holding.code == code).all()

def fetch_hist_price(code, start_date, end_date = ''):
    start_date, end_date, code = process_params(start_date, end_date, code)
    return Hist_price.query.filter(Hist_price.dt >= start_date, Hist_price.dt <= end_date, Hist_price.code == code).all()

def fetch_all_hist_price():
    return Hist_price.query.all()

def delete_holding(start_date, end_date = ''):
    start_date, end_date, code = process_params(start_date, end_date, '')
    sql = sqls.get_sql('delete_hld_by_day', start_date, end_date)
    db.session.execute(sql)
    db.session.commit()

def delete_asset(start_date, end_date = ''):
    start_date, end_date, code = process_params(start_date, end_date, '')
    sql = sqls.get_sql('delete_ast_by_day', start_date, end_date)
    db.session.execute(sql)
    db.session.commit()

def load_holding_data(path, date_start, date_end):
    load_data(path, 't_holding', date_start, date_end)

def load_data(path, table, date_start, date_end):
    try:
        sql_template = sqls.sql_dict['load_data']
        sql = sql_template % (path, table)
        db.session.execute(sql)
        db.session.commit()
    except Exception, e:
        traceback.print_exc()

def process_params(start_date, end_date, code):
    if ((start_date == '' and code == '')
        or (end_date <> '' and end_date < start_date)
        or start_date == None
        or end_date == None
        or code == None):
        return []
    if end_date == '':
        end_date = start_date
    return (start_date, end_date, code)

def init_holding():
    hlds = []
    hld = Holding(dt = '2016-01-01',
                  portfolio = 'freedom',
                  code = '-',
                  sec_type = 'cash',
                  quantity = 100000,
                  amount = 100000)
    hlds.append(hld)
    hld = Holding(dt = '2016-01-01',
                  portfolio = 'other',
                  code = '-',
                  sec_type = 'cash',
                  quantity = 0,
                  amount = 0)
    hlds.append(hld)
    hld = Holding(dt = '2016-01-01',
                  portfolio = 'oth_funds',
                  code = '-',
                  sec_type = 'cash',
                  quantity = 300000,
                  amount = 300000)
    hlds.append(hld)
    hld = Holding(dt = '2016-01-01',
                  portfolio = 'ss50_fund',
                  code = '-',
                  sec_type = 'cash',
                  quantity = 100000,
                  amount = 100000)
    hlds.append(hld)
    hld = Holding(dt = '2016-01-01',
                  portfolio = 'ss50_lowestpb',
                  code = '-',
                  sec_type = 'cash',
                  quantity = 500000,
                  amount = 500000)
    hlds.append(hld)
    db.session.add_all(hlds)
    db.session.commit()

if __name__ == '__main__':
    print 'main'
    #create_tables()
    init_holding()

    #import_code_prc('../../../data/code_price.txt')

    #add_user('leidayu', 'leidayu', 'leidayu@123.com', 'admin')

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

    # fetch holding
    #holdings = fetch_holding('2016-03-07', code = '')
    #print holdings

    #hist_price = fetch_hist_price('600029', '2018-09-21')
    #if len(hist_price) > 0:
    #    print hist_price[0].price * 1000