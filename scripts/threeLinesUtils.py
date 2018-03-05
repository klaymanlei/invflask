#coding:utf-8

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
        return prs(td.date, lastData.co, max(lastData.co, td.cl), min(lastData.co, td.co),  td)
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

'''
p1 = prs(2.0, 5.0, 2.0, 5.0)
p2 = prs(5.0, 8.0, 5.0, 8.0)
p3 = prs(8.0, 11.0, 8.0, 11.0)

print cal([p1, p2, p3], 12.0, 3)
'''
