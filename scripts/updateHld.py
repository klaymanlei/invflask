#coding:utf-8
import sys
import utils_db 
import utils

from pu import *
from config_script import *

def fetch_hld_yesterday(date_str):
    date_1 = utils.lastday(date_str)
    hlds = utils_db.fetch_hld(date_1)
    hld_dict = {}
    if len(hlds) == 0:
        return hld_dict
    for hld in hlds:
        hld.date = date_str 
        hld_dict[hld.code] = hld
    return hld_dict

date_str = TODAY
if len(sys.argv) == 2:
    date_str = sys.argv[1]

hlds = fetch_hld_yesterday(date_str)
trds = utils_db.fetch_trd(date_str)

for trd in trds:
    hld_c = hlds['0']
    hld = None
    if hlds.has_key((trd.code, trd.portfolio)):
        hld = hlds[(trd.code, trd.portfolio)]
    else:
        hld = hld_pu()
        hlds[(trd.code, trd.portfolio)] = hld
        hld.date = trd.date
        hld.portfolio = trd.portfolio
        hld.code = trd.code
        hld.name = trd.name
    hld.share = hld.share + trd.share
    hld.cost = hld.cost + trd.cst + trd.share * trd.prc
    hld_c.share = hld_c.share - trd.cst - trd.share * trd.prc
    hld_c.cost = hld_c.share

utils_db.delete_hld(date_str)
utils_db.save_hld(hlds)    
