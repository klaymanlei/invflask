#coding:utf-8
import MySQLdb
import traceback

import sqls
from pu import *
from config_script import *

def fetch_trd(date_str):
    try:
        trds = []
        sql = sqls.get_sql('trd_by_day', date_str)
        # print sql
        rows = query(sql)
        # print rows
        for row in rows:
            trd = trd_pu()
            trd.date = row[0]
            trd.code = row[1]
            trd.name = row[2]
            trd.share = row[3]
            trd.prc = row[4]
            trd.cst = row[5]
            trds.append(trd)
        # print hlds
        return trds
    except Exception, e:
        print "Error occured"
        traceback.print_exc()

def fetch_hld(date_str):
    try:
        hlds = []
        sql = sqls.get_sql('hld_by_day', date_str)
        # print sql
        rows = query(sql)
        # print rows
        for row in rows:
            hld = hld_pu()
            hld.date = row[0]
            hld.code = row[1]
            hld.name = row[2]
            hld.share = row[3]
            hld.cost = row[4]
            hlds.append(hld)
        # print hlds
        return hlds
    except Exception, e:
        print "Error occured"
        traceback.print_exc()

def delete_hld(date_str):
    try:
        sql = sqls.get_sql('delete_hld_by_day', date_str)
        update(sql)
    except Exception, e:
        traceback.print_exc()

def save_hld(hlds):
    try:
        sql_template = sqls.sql_dict['save_hld']
        for code,hld in hlds.items():
            sql = sql_template % hld.to_tuple() 
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

