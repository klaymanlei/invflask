#coding: utf-8

import os

import utils_db
import utils
from pu import *

def update_holding_by_date(date_start, date_end):
    all_trans = all_trans_between(date_start, date_end)
    date = utils.date_add(date_start, -1)
    hlds = utils_db.fetch_holding(date)

    path = '../tmp/hlds_' + date_start + '_' + date_end + '.txt'
    if os.path.exists(path):
        os.remove(path)

    while date < date_end:
        date = utils.date_add(date, 1)
        print date
        #utils_db.delete_hld(date)
        trans_list = all_trans.get(date)

        hlds_dict = {}
        for hld in hlds:
            hld.date = date
            if hld.sec_type == 'cash':
                hlds_dict[(hld.portfolio, hld.sec_type)] = hld
            else:
                hlds_dict[(hld.portfolio, hld.code)] = hld

        #print hlds_dict
        if trans_list != None:
            update_hold_dict(hlds_dict, trans_list)
            hlds = hlds_dict.values()
            #print trans_list
            #print hlds_dict

        output_hlds(hlds_dict, path)

    utils_db.delete_hld(date_start, date_end)
    utils_db.hld_load_data(path, date_start, date_end)

def output_hlds(hlds_dict, path):
    file = open(path , 'a+')
    split_str = '\t'
    lines = ''
    for hld in hlds_dict.values():
        lines += split_str.join(hld.to_str_tuple())
        lines += '\n'
    file.write(lines)
    file.close()
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
    hld = holding()
    hld.date = trans.date
    hld.portfolio = trans.portfolio
    hld.code = trans.code
    hld.sec_type = trans.sec_type
    return hld

def all_trans_between(date_start, end_date):
    all_trans = utils_db.fetch_transaction(date_start, end_date)
    trans_dict = {}
    for trans in all_trans:
        trans_list = trans_dict.get(trans.date)
        if trans_list == None:
            trans_list = []
            trans_dict[trans.date] = trans_list
        trans_list.append(trans)
    return trans_dict

update_holding_by_date('2016-01-02', '2018-10-10')
#for trans in trans_list:
#    key = (trans.date, trans.code, trans.portfolio)
#    hld = hlds.get(key)
#    if  hld == None:
#        hld = holding()
#        hld.date = trans.date
#        hld.portfolio = trans.portfolio
#        hld.code = trans.code
#        hlds[key] = hld
#    hld.quantity += trans.quantity
#    hld.amount -= trans.amount
    #print hlds

