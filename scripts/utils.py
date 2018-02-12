#coding:utf-8
import datetime
import time

def lastday(date_str):
    datet = time.strptime(date_str, '%Y-%m-%d')
    date = datetime.datetime(datet.tm_year, datet.tm_mon, datet.tm_mday)
    lastday = date + datetime.timedelta(days = -1)
    return lastday.strftime('%Y-%m-%d') 

def read_file(file_path):
    file_in = open(file_path, 'r')
    data = []
    for line in file_in:
        if len(line.strip()) > 0:
            data.append(line.strip().split('\t'))
    file_in.close()
    return data

def get_type(code):
    if code == '0':
        return 'c'
    elif len(code) == 6:
        if code[0] == '6' or code[0] == '2' or code[0] == '0' or code[0] == '3':
            return 'st'
    return '-'

# print lastday('2016-03-01')
