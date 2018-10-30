#coding:utf-8
import sys
import MySQLdb
import traceback

import sqls
from pu import *
from config_script import *

reload(sys)
sys.setdefaultencoding('utf8')

def fetch_transaction(date_start, date_end = ''):
    if date_end == '':
        date_end = date_start
    try:
        trans_list = []
        sql = sqls.get_sql('trans_by_day', date_start, date_end)
        # print sql
        rows = query(sql)
        # print rows
        for row in rows:
            trans = transaction()
            trans.date = str(row[0])
            trans.code = row[1]
            trans.operation = row[2]
            trans.portfolio = row[3]
            trans.sec_type = row[4]
            trans.quantity = float(row[5])
            trans.price = float(row[6])
            trans.tax = float(row[7])
            trans.other_charges = float(row[8])
            trans.amount = float(row[9])
            trans_list.append(trans)
        #print trans_list[0]
        return trans_list
    except Exception, e:
        print "Error occured"
        traceback.print_exc()

def fetch_holding(date_start, date_end = ''):
    if date_end == '':
        date_end = date_start
    try:
        hlds = []
        sql = sqls.get_sql('hld_by_day', date_start, date_end)
        # print sql
        rows = query(sql)
        # print rows
        for row in rows:
            hld = holding()
            hld.date = row[0]
            hld.portfolio = row[1]
            hld.code = row[2]
            hld.sec_type = row[3]
            hld.quantity = float(row[4])
            hld.amount = float(row[5])
            hlds.append(hld)
        # print hlds
        return hlds
    except Exception, e:
        print "Error occured"
        traceback.print_exc()

def delete_hld(date_start, date_end):
    try:
        sql = sqls.get_sql('delete_hld_by_day', date_start, date_end)
        update(sql)
    except Exception, e:
        traceback.print_exc()

def save_hld(hlds):
    try:
        sql_template = sqls.sql_dict['save_hld']
        for (portfolio, code), hld in hlds.items():
            sql = sql_template % hld.to_tuple()
            #print sql
            update(sql)
    except Exception, e:
        traceback.print_exc()

def hld_load_data(path, date_start, date_end):
    load_data(path, 't_holding', date_start, date_end)

def load_data(path, table, date_start, date_end):
    try:
        sql_template = sqls.sql_dict['load_data']
        sql = sql_template % (path, table)
        print sql
        update(sql)
    except Exception, e:
        traceback.print_exc()


def delete_ast(date_str):
    try:
        sql = sqls.get_sql('delete_ast_by_day', date_str)
        update(sql)
    except Exception, e:
        traceback.print_exc()

def save_ast(asts):
    try:
        sql_template = sqls.sql_dict['save_ast']
        for ast in asts:
            sql = sql_template % ast.to_tuple()
            update(sql)
    except Exception, e:
        traceback.print_exc()

def query(sql):
    db = connect()
    cursor = db.cursor() 
    cursor.execute(sql)
    rows = cursor.fetchall()
    db.close()
    return rows

def update(sql):
    db = connect()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
 
def connect():
    db = MySQLdb.connect(
        host = DB_SERVER, 
        port = DB_PORT, 
        user = DB_USER, 
        passwd = DB_PW, 
        charset = 'utf8', 
        db = DB
    )
    return db

