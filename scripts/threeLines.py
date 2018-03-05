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
            print data[1]
            maxDate = data[1]
            lastClose = threeLinesUtils.prs(data[1], float(data[2]), float(data[3]), float(data[4]), float(data[5]))
    file.close()
    return lastClose

def hist(code, outFolder, dateStr, threhold):
    hists = []
    if not os.path.exists(code + '.3ls') or threhold < 2:
        return hists
    file = open(code + '.3ls', 'r')
    maxDate = ''
    for line in file:
        data = line.strip().split(',')
        prs = threeLinesUtils.prs(data[0], float(data[1]), float(data[2]), float(data[3]), float(data[4]))
        if prs.date > dateStr:
            continue
        if len(hists) == 0:
            hists.append(prs)       
            continue
        if prs.date < hists[0].date:
            continue
        i = 0
        for i in range(0, len(hists) + 1):
            if i == len(hists):
                hists.append(prs)
                break
            hist = hists[i] 
            if hist.date > prs.date:
                hists.insert(i, prs)
                break
        if len(hists) > threhold:
            del hists[0]
    file.close()
    return hists

def write(prs, outFolder):
    file = open(code + '.3ls', 'a')
    file.write('%s,%.3f,%.3f,%.3f,%.3f\n' % (prs.date, prs.op, prs.hi, prs.lo, prs.co))

newClose = lastClose(code, dataFolder, dateStr)
hists = hist(code, outFolder, dateStr, 3)
write(newClose, outFolder)

