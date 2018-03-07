#coding: utf-8

import os
import sys
import threeLinesUtils
import utils

if len(sys.argv) != 3:
    print 'Usage: python %s %s' % (sys.argv[0], '<code> <yyyy-mm-dd>')
    exit()
else:
    code = sys.argv[1]
    dateStr = sys.argv[2]

dataFolder = './'
outFolder = './'

def lastClose(code, dataFolder, dateStr):
    season = utils.get_season(dateStr)
    file = open(dataFolder + season, 'r')

    maxDate = ''
    lastClose = None 
    for line in file:
        if not ',' in line or line[:6] != code:
            continue
        data = line.strip().split(',')
        if data[1] > dateStr:
            continue
        if data[1] > maxDate:
            # print data[1]
            maxDate = data[1]
            lastClose = threeLinesUtils.prs(data[1], float(data[2]), float(data[3]), float(data[4]), float(data[5]))
    file.close()
    #if lastClose.op == lastClose.co:
    #    return None
    #else:
    return lastClose

dateStr = '2016-01-11'
newClose = lastClose(code, dataFolder, dateStr)
print '=========new rec========='
print newClose
if newClose == None:
    exit()
hists = threeLinesUtils.hist(code, code + '.3ls', outFolder, dateStr, 3)
print '=========hists========='
for hist in hists:
    print hist

if len(hists) > 0:
    td = threeLinesUtils.cal(hists, newClose, 3)
else:
    if newClose.op == newClose.co:
        td = None
    else:
        newClose.hi = max(newClose.op, newClose.co)
        newClose.lo = min(newClose.op, newClose.co)
        td = newClose

print '=========res========='
print td
if td != None:
    threeLinesUtils.write(td, outFolder, code)

