#coding:utf-8
from utils_db import *
from scripts.config_script import *

date_str = TODAY

def read_3ls(fileName):
    fileIn = open('scripts/' + fileName, 'r')
    res = []
    for line in fileIn:
        data = line.strip().split(',')
        res.append((data[0], (data[1], data[4], data[3], data[2])))
    fileIn.close()
    return res

def getFileName(code, period):
    if period == 'day':
        return code + '.3ls'
    if period == 'week':
        return code + '.3lsw'
    if period == 'month':
        return code + '.3lsm'
    return None

def candles(code, period):
    fileName = getFileName(code, period)
    recs = read_3ls(fileName)
    data = []
    dates = []
    for rec in recs:
        #data.append({'value':(rec[0], rec[1])})
        data.append(rec[1])
        dates.append(rec[0])
    json_dict = [['total', '2', '3', '4'], [{'name': 'total', 
        'type': 'candlestick', 
        #'type': 'line',
        'itemStyle': {
            'normal': {
                'color': '#FD1050',
                'color0': '#0CF49B',
                'borderColor': '#FD1050',
                'borderColor0': '#0CF49B'
            }
        },
        #'showSymbol': False,
        #'hoverAnimation': False,
        'data': data}], dates]
    return json_dict 

#res = candles('510050', 'day')
#for line in res:
#    print line
