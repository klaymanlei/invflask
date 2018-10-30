#coding:utf-8

sql_dict = {}
sql_dict['hld_by_day'] = """
select dt,portfolio,code,sec_type,quantity,amount from t_holding where dt between '${date_start}' and '${date_end}'
"""
sql_dict['trans_by_day'] = """
select dt,code,operation,portfolio,sec_type,quantity,price,tax,other_charges,amount 
from t_transaction where dt between '${date_start}' and '${date_end}'
order by dt,code,operation
"""
sql_dict['delete_hld_by_day'] = """
delete from t_holding where dt between '${date_start}' and '${date_end}'
"""
sql_dict['save_hld'] = """
INSERT INTO invdb.t_holding (dt, portfolio, code, sec_type, quantity, amount)
VALUES ('%s', '%s', '%s', '%s', '%f', '%f')
"""
sql_dict['delete_ast_by_day'] = """
delete from t_ast where dt between '${date_start}' and '${date_end}'
"""
sql_dict['save_ast'] = """
INSERT INTO invdb.t_ast (dt, portfolio, CODE, NAME, TYPE, SHARE, prc)
VALUES ('${date_start}', '%s', '%s', '%s', '%s', '%f', '%f')
"""
sql_dict['total_ast'] = """
select dt, 'total', round(sum(value), 2)
from invdb.ast_overview where dt between '${date_start}' and '${date_end}' group by dt
"""
sql_dict['load_data'] = """
load data local infile '%s' into table %s;
"""

def get_sql(name, date_start, date_end):
    if sql_dict.has_key(name):
        sql = sql_dict[name]
        sql = sql.replace('${date_start}', date_start)
        return sql.replace('${date_end}', date_end)
    return ''

