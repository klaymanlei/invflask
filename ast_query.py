#coding:utf-8
from utils_db import *
from scripts.config_script import *

date_str = TODAY

def ast_line():
    recs = fetch_total_ast(date_str)
    data = []
    for rec in recs:
        data.append({'value':(rec[0], rec[2])})
    json_dict = [['total'], [{'name': 'total', 
        'type': 'line', 
        'showSymbol': False,
        'hoverAnimation': False,
        'data': data}]]
    return json_dict 
