#coding:utf-8

sql_dict = {}
sql_dict['hld_by_day'] = """
select dt,code,name,share,cost from t_hld where dt='${date}'
"""
sql_dict['trd_by_day'] = """
select dt,code,name,share,prc,cst from t_trd where dt='${date}'
"""
sql_dict['delete_hld_by_day'] = """
delete from t_hld where dt='${date}'
"""
sql_dict['save_hld'] = """
INSERT INTO invdb.t_hld (dt, CODE, NAME, SHARE, cost)
VALUES ('%s', '%s', '%s', '%f', '%f')
"""

def get_sql(name, date):
    if sql_dict.has_key(name):
        sql = sql_dict[name]
        return sql.replace('${date}', date)
    return ''
