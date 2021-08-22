#encoding=utf-8
#!/usr/bin/python

import traceback
import MySQLdb

from constants import *

table_name = 'ads_securities_3line'

# 连接数据库
def connect():
    try:
        db = MySQLdb.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, passwd=DB_PASSWD, db=DB_NAME, charset='utf8')
    except Exception, e:
        print "Could not connect to MySQL server."
        print e
        exit(0)
    return db

# 查询日期小于date参数的历史记录，其中code为证券代码，type为反转类型（day、week或者month），line_cnt为返回数据量，默认为3
# 返回结果按时间倒序排列
def get_hist(date, code, type, line_cnt = 3):
    rows = []
    db = connect()
    try:
        cursor = db.cursor()
        sql = """
            select 
                date, code, open, close 
            from
                ${table_name}
            where 
                date < '%s'
                and code = '%s'
                and type = '%s'
            order by date desc
            limit %d 
        """ % (date, code, type, line_cnt)
        sql = sql.replace('${table_name}', table_name)
        print sql
        cursor.execute(sql)
        for row in cursor.fetchall():
            data = {}
            data['date'] = str(row[0])
            data['code'] = str(row[1])
            data['open'] = float(row[2])
            data['close'] = float(row[3])
            rows.append(data)
    except Exception, e:
        print "[info] errer !"
        print e
        print traceback.format_exc()
    finally:
        cursor.close()
        db.close()
    return rows

# 删除给定证券代码（code）及给定反转类型（type）在给定日期（date）及之后的所有记录
def clean_after(date, code, type):
    db = connect()
    try:
        cursor = db.cursor()
        sql = """
            delete
            from
                ${table_name}
            where 
                date >= '%s'
                and code = '%s'
                and type = '%s'
        """ % (date, code, type)
        sql = sql.replace('${table_name}', table_name)
        #print sql
        cursor.execute(sql)
        db.commit()
    except Exception, e:
        print "[info] errer !"
        print e
        print traceback.format_exc()
    finally:
        cursor.close()
        db.close()

# 将给定的证券代码（code）、反转类型（type）、给定日期（date）及开盘收盘价格插入数据库
def insert(date, code, type, open, close):
    db = connect()
    try:
        cursor = db.cursor()
        sql = """
            insert into ${table_name} (type, date, code, open, close)
            values (%s, %s, %s, %s, %s)
        """
        sql = sql.replace('${table_name}', table_name)
        #print sql
        cursor.execute(sql, (type, date, code, open, close))
        db.commit()
    except Exception, e:
        print "[info] errer !"
        print e
        print traceback.format_exc()
    finally:
        cursor.close()
        db.close()

if __name__ == '__main__':
    hist = get_hist('2021-08-20', '510500', 'week', 3)
    #clean_after('2021-06-01', '510500', 'week')
    #insert('2021-06-04', '510500', 'week', 7.427, 7.465)
    print hist


