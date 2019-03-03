#coding: utf-8

import os

from db.mysql.mysql_utils import *
import utils
from pu import *

def update_asset_by_date(date_start, date_end, hist_price_dict):
    all_holding = all_holding_between(date_start, date_end)
    date = utils.date_add(date_start, -1)
    delete_asset(date_start, date_end)
    #hlds = fetch_holding(date)
    asset_output = []

    #path = '../tmp/hlds_' + date_start + '_' + date_end + '.txt'
    #if os.path.exists(path):
    #    os.remove(path)

    while date < date_end:
        date = utils.date_add(date, 1)
        #print date
        holding_list = all_holding.get(date)

        # asset_dict = {portfolio, amount}
        asset_dict = {}

        for hld in holding_list:
            asset_tmp = Asset(dt = date, portfolio = hld.portfolio, code = hld.code,
                              sec_type = hld.sec_type, quantity = hld.quantity, amount = hld.amount)
            if asset_tmp.sec_type == 'cash':
                asset_dict[(asset_tmp.portfolio, asset_tmp.sec_type)] = asset_tmp
            else:
                q = asset_tmp.quantity
                tmp_date = date
                while (not hist_price_dict.has_key((asset_tmp.code, tmp_date))):
                    if tmp_date < '2016-01-01':
                        break
                    tmp_date = utils.date_add(tmp_date, -1)
                if tmp_date < '2016-01-01':
                    hist_price = 0
                else:
                    hist_price = float(hist_price_dict[(asset_tmp.code, tmp_date)])
                asset_tmp.amount = q * hist_price
                #if date == '2018-05-31':
                #    print asset_tmp
                #    print hld
                #    print
                #if len(hist_price) > 0:
                #    asset_tmp.amount = q * hist_price[0].price
                asset_dict[(asset_tmp.portfolio, asset_tmp.code)] = asset_tmp

        print date
        #print asset_dict
        #if holding_list != None:
        #    update_hold_dict(asset_dict, holding_list)
        #    hlds = asset_dict.values()
        save_all_asset(asset_dict.values())
        #append_hlds(asset_dict, asset_output)

    #for hld in asset_output:
    #    print hld

    #save_all_asset(asset_output)

def append_hlds(hlds_dict, hlds_output):
    for hld in hlds_dict.values():
        hlds_output.append(hld)
    return

def update_hold_dict(asset_dict, holding_list):
    for holding in holding_list:
        cash = asset_dict.get((holding.portfolio, 'cash'))
        if holding.code != '-':
            hld = asset_dict.get((holding.portfolio, holding.code))
            if hld == None:
                hld = create_holding(holding)
                asset_dict[(hld.portfolio, hld.code)] = hld
            hld.quantity += holding.quantity
            hld.amount -= holding.amount
            if hld.quantity == 0:
                asset_dict.pop((hld.portfolio, hld.code))
        cash.quantity += holding.amount
        cash.amount = cash.quantity

def create_holding(trans):
    hld = Holding(dt = trans.dt, portfolio = trans.portfolio, code=trans.code,
                  sec_type = trans.sec_type, quantity = 0.0, amount = 0.0)
    return hld

def all_holding_between(date_start, end_date):
    all_holding = fetch_holding(date_start, end_date)
    holding_dict = {}
    for holding in all_holding:
        holding_list = holding_dict.has_key(holding.dt.strftime("%Y-%m-%d")) and holding_dict[holding.dt.strftime("%Y-%m-%d")] or []
        holding_list.append(holding)
        holding_dict[holding.dt.strftime("%Y-%m-%d")] = holding_list
    return holding_dict

hist_prices = fetch_all_hist_price()
hist_price_dict = {}
for hist_price in hist_prices:
    hist_price_dict[(hist_price.code, str(hist_price.dt))] = hist_price.price
update_asset_by_date('2016-01-01', '2018-10-10', hist_price_dict)

#holdings = all_holding_between('2016-01-02', '2018-10-10')
#for holding in holdings:
#    print holdings[holding]