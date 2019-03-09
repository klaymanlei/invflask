#coding:utf-8
from utils_db import *
from scripts.config_script import *
import scripts.utils

date_str = TODAY

def ast_line():
    date_end = utils.date_add(date_str, -62)
    recs = fetch_total_ast(date_str)
    data = []
    dates = []
    for rec in recs:
        #data.append({'value':(rec[0], rec[2])})
        data.append(rec[2])
        dates.append(rec[0])
    json_dict = [['total'], [{'name': 'total', 
        'type': 'line', 
        'showSymbol': False,
        'hoverAnimation': False,
        'data': data}], dates]
    return json_dict 
