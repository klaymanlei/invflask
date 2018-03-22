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

dataFolder = '/home/hadoop/data/seasondata/'
outFolder = '/home/hadoop/python/vflask/invflask/data/'

#dateStr = '2016-01-11'
newClose = threeLinesUtils.lastClose(code, dataFolder, dateStr)
print '=========new rec========='
print newClose
if newClose == None:
    exit()
hists = threeLinesUtils.hist(outFolder + code + '.3lsm', dateStr, 2, utils.before_month)
print '=========hists========='
for hist in hists:
    print hist

if len(hists) > 0:
    td = threeLinesUtils.cal(hists, newClose, 2)
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
    threeLinesUtils.write(td, outFolder + code + '.3lsm', dateStr, utils.before_month)
