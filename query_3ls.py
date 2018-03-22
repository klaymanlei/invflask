#coding:utf-8
from utils_db import *
from scripts.config_script import *

date_str = TODAY

def read_3ls(fileName):
    fileIn = open('data/' + fileName, 'r')
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
        #data.append(rec[1])
        data.append(rec[1][1])
        dates.append(rec[0])
        if len(data) > 62:
            data.pop(0)
            dates.pop(0)
    json_dict = [[], [{'name': period + '_k', 
        #'type': 'candlestick', 
        'type': 'line',
        'itemStyle': {
            'normal': {
                'color': '#DD3333',
                'color0': '#33DD66',
                'borderColor': '#DD3333',
                'borderColor0': '#33DD66'
            }
        },
        #'showSymbol': False,
        #'hoverAnimation': False,
        'data': data}], dates]
    return json_dict 

#res = candles('510050', 'day')
#for line in res:
#    print line
