#coding:utf-8

import os

class prs:
    def __init__(self, date, op, hi, lo, co):
        if hi < op or hi < co:
            raise AttributeError("invalid hi value")
        if lo > op or lo > co:
            raise AttributeError("invalid lo value")
        self.date = date
        self.op = op
        self.hi = hi
        self.lo = lo
        self.co = co

    def __str__(self):
        return '{prs: (%s, %.3f, %.3f, %.3f, %.3f)}' % (self.date, self.op, self.hi, self.lo, self.co)

def cal(hist, td, threhold):
    if not validHist(hist, threhold) or not isinstance(td, prs):
        return None
    lastData = hist[-1]
    if td.co == lastData.co:
        return None
    if (lastData.co - lastData.op) * (td.co - lastData.co) > 0:
        return prs(td.date, lastData.co, max(lastData.co, td.co), min(lastData.co, td.co),  td.co)
    firstData = hist[0]
    if (lastData.co - lastData.op) * (firstData.op - td.co) > 0:
        return prs(td.date, lastData.op, max(lastData.op, td.co), min(lastData.op, td.co), td.co)
    return None

def validHist(hist, threhold):
    if threhold < 2:
        return False
    if not type(hist) is list:
        return False
    if len(hist) > threhold or len(hist) == 0:
        return False
    diff = 0
    for data in hist:
        if  not isinstance(data, prs):
            return False
        if diff * (data.co - data.op) < 0:
            return False
        diff = data.co - data.op
    return True

def hist(code, histFile, outFolder, dateStr, threhold):
    hists = []
    if not os.path.exists(histFile) or threhold < 2:
        return hists
    file = open(histFile, 'r')
    maxDate = ''
    for line in file:
        data = line.strip().split(',')
        prsIn = prs(data[0], float(data[1]), float(data[2]), float(data[3]), float(data[4]))
        if prsIn.date > dateStr:
            continue
        if len(hists) == 0:
            hists.append(prsIn)
            continue
        if len(hists) == threhold and prsIn.date < hists[0].date:
            continue
        i = 0
        for i in range(0, len(hists) + 1):
            if i == len(hists):
                hists.append(prsIn)
                break
            hist = hists[i]
            if hist.date > prsIn.date:
                hists.insert(i, prsIn)
                break
        if len(hists) > threhold:
            del hists[0]
    file.close()
    if len(hists) == 0:
        return hists

    dir = hists[-1].co - hists[-1].op
    i = len(hists) - 1
    while i >= 0:
        if (hists[i].co - hists[i].op) * dir < 0:
            break
        i -= 1
    return hists[i + 1 : ]

def write(prs, outFolder, code):
    file = open(code + '.3ls', 'a')
    file.write('%s,%.3f,%.3f,%.3f,%.3f\n' % (prs.date, prs.op, prs.hi, prs.lo, prs.co))

'''
p1 = prs(2.0, 5.0, 2.0, 5.0)
p2 = prs(5.0, 8.0, 5.0, 8.0)
p3 = prs(8.0, 11.0, 8.0, 11.0)

print cal([p1, p2, p3], 12.0, 3)
'''
