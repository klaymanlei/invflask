#coding:utf-8

sql_dict = {}
sql_dict['hld_by_day'] = """
select dt,portfolio,code,name,share,cost from t_hld where dt='${date}'
"""
sql_dict['trd_by_day'] = """
select dt,code,name,portfolio,share,prc,cst from t_trd where dt='${date}'
"""
sql_dict['delete_hld_by_day'] = """
delete from t_hld where dt='${date}'
"""
sql_dict['save_hld'] = """
INSERT INTO invdb.t_hld (dt, portfolio, CODE, NAME, SHARE, cost)
VALUES ('%s', '%s', '%s', '%s', '%f', '%f')
"""
sql_dict['delete_ast_by_day'] = """
delete from t_ast where dt='${date}'
"""
sql_dict['save_ast'] = """
INSERT INTO invdb.t_ast (dt, portfolio, CODE, NAME, TYPE, SHARE, prc)
VALUES ('%s', '%s', '%s', '%s', '%s', '%f', '%f')
"""

def get_sql(name, date):
    if sql_dict.has_key(name):
        sql = sql_dict[name]
        return sql.replace('${date}', date)
    return ''
