#coding:utf-8

import sys

import utils
import utils_db

from pu import *
from config_script import *

date_str = TODAY
if len(sys.argv) == 2:
    date_str = sys.argv[1]

records = utils.read_file('2018-01-01')
prc_dict = {}
for rec in records:
    if rec[0] == date_str and len(rec) == 7:
        prc_dict[rec[1]] = rec[-2]

hlds = utils_db.fetch_hld(date_str)
asts = []
for hld in hlds:
    ast = ast_pu()
    ast.date = hld.date
    ast.code = hld.code
    ast.name = hld.name
    ast.type = utils.get_type(ast.code)
    ast.share = hld.share
    if hld.code == '0':
        ast.prc = 1.0
    else: 
        ast.prc = float(prc_dict[ast.code])
    asts.append(ast)

utils_db.delete_ast(date_str)
utils_db.save_ast(asts)
