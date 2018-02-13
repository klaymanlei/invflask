#coding:utf-8
import traceback

from scripts.utils_db import query,update
import scripts.sqls

def fetch_total_ast(date_str):
    try:
        asts = []
        sql = scripts.sqls.get_sql('total_ast_before', date_str)
        print "sql:", sql
        rows = query(sql)
        for row in rows:
            ast = (str(row[0]), row[1], str(row[2]))
            asts.append(ast) 
        print asts
        return asts
    except Exception, e:
        print "Error occured"
        traceback.print_exc()

#def query(sql):
#    return scripts.utils_db.query(sql)

#def update(sql):
#    scripts.utils_db.update(sql)

