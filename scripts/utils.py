#coding:utf-8
import datetime
import time

def lastday(date_str):
    datet = time.strptime(date_str, '%Y-%m-%d')
    date = datetime.datetime(datet.tm_year, datet.tm_mon, datet.tm_mday)
    lastday = date + datetime.timedelta(days = -1)
    return lastday.strftime('%Y-%m-%d') 

# print lastday('2016-03-01')
