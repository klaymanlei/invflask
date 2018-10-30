#coding:utf-8
import datetime
import time

def lastday(date_str):
    return date_add(date_str, -1)

def date_add(date_str, delta = 1):
    datet = time.strptime(date_str, '%Y-%m-%d')
    date = datetime.datetime(datet.tm_year, datet.tm_mon, datet.tm_mday)
    target = date + datetime.timedelta(days = delta)
    return target.strftime('%Y-%m-%d')

def read_file(file_path, split_char):
    file_in = open(file_path, 'r')
    data = []
    for line in file_in:
        if len(line.strip()) > 0:
            data.append(line.strip().split(split_char))
    file_in.close()
    return data

def get_type(code):
    if code == '0':
        return 'c'
    elif len(code) == 6:
        if code[0] == '6' or code[0] == '2' or code[0] == '0' or code[0] == '3':
            return 'st'
    return '-'

def get_season(date_str):
    strs = date_str.split('-')
    if len(strs) != 3:
        return date_str
    mon = int(strs[1])
    season_mon = mon - (mon + 2) % 3
    return "%s-%02d-01" % (strs[0], season_mon)

def is_weekend(date_str):
    datet = time.strptime(date_str, '%Y-%m-%d')
    date = datetime.datetime(datet.tm_year, datet.tm_mon, datet.tm_mday)
    weekday = date.weekday()
    return weekday > 4

def last_friday(date_str):
    if is_weekend(date_str):
        date_str = lastday(date_str)
    if is_weekend(date_str):
        date_str = lastday(date_str)
    return date_str

def parse_date(dateStr):
    return datetime.datetime.strptime(dateStr, '%Y-%m-%d')

def before_day(dateStr1, dateStr2):
    date1 = parse_date(dateStr1)
    date2 = parse_date(dateStr2)
    return date2 < date1

def before_week(dateStr1, dateStr2):
    date1 = parse_date(dateStr1)
    date2 = parse_date(dateStr2)
    return date2.strftime('%Y%W') < date1.strftime('%Y%W')

def before_month(dateStr1, dateStr2):
    date1 = parse_date(dateStr1)
    date2 = parse_date(dateStr2)
    return date2.strftime('%Y%m') < date1.strftime('%Y%m')

