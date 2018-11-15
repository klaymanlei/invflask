#coding: utf-8

import os

from db.mysql.mysql_utils import *
import utils
from pu import *

def update_holding_by_date(date_start, date_end):
    all_trans = all_trans_between(date_start, date_end)
    date = utils.date_add(date_start, -1)
    hlds = fetch_holding(date)
    hlds_output = []

    #path = '../tmp/hlds_' + date_start + '_' + date_end + '.txt'
    #if os.path.exists(path):
    #    os.remove(path)

    while date < date_end:
        date = utils.date_add(date, 1)
        #print date
        #utils_db.delete_hld(date)
        trans_list = all_trans.get(date)

        hlds_dict = {}
        for hld in hlds:
            hld_tmp = Holding(dt = date, portfolio = hld.portfolio, code = hld.code,
                              sec_type = hld.sec_type, quantity = hld.quantity, amount = hld.amount)
            if hld_tmp.sec_type == 'cash':
                hlds_dict[(hld_tmp.portfolio, hld_tmp.sec_type)] = hld_tmp
            else:
                hlds_dict[(hld_tmp.portfolio, hld_tmp.code)] = hld_tmp

        #print hlds_dict
        if trans_list != None:
            update_hold_dict(hlds_dict, trans_list)
            hlds = hlds_dict.values()
            #print trans_list
            #print hlds_dict

        append_hlds(hlds_dict, hlds_output)

    delete_holding(date_start, date_end)
    #for hld in hlds_output:
    #    print hld
    save_all_holdings(hlds_output)

def append_hlds(hlds_dict, hlds_output):
    for hld in hlds_dict.values():
        hlds_output.append(hld)
    return

def update_hold_dict(hlds_dict, trans_list):
    for trans in trans_list:
        hld_cash = hlds_dict.get((trans.portfolio, 'cash'))
        if trans.code != '-':
            hld = hlds_dict.get((trans.portfolio, trans.code))
            if hld == None:
                hld = create_holding(trans)
                hlds_dict[(hld.portfolio, hld.code)] = hld
            hld.quantity += trans.quantity
            hld.amount -= trans.amount
            if hld.quantity == 0:
                hlds_dict.pop((hld.portfolio, hld.code))
        hld_cash.quantity += trans.amount
        hld_cash.amount = hld_cash.quantity

def create_holding(trans):
    hld = Holding(dt = trans.dt, portfolio = trans.portfolio, code=trans.code,
                  sec_type = trans.sec_type, quantity = 0.0, amount = 0.0)
    return hld

def all_trans_between(date_start, end_date):
    all_trans = fetch_transaction(date_start, end_date)
    trans_dict = {}
    for trans in all_trans:
        trans_list = trans_dict.has_key(trans.dt.strftime("%Y-%m-%d")) and trans_dict[trans.dt.strftime("%Y-%m-%d")] or []
        trans_list.append(trans)
        trans_dict[trans.dt.strftime("%Y-%m-%d")] = trans_list
    return trans_dict

update_holding_by_date('2016-01-02', '2018-10-10')

#trans_dict = all_trans_between('2016-01-02', '2018-10-10')
#for (key, value) in trans_dict.items():
#    print key, value
