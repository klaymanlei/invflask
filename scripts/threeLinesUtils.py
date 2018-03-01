#coding:utf-8

class prs:
    def __init__(self, op, hi, lo, co):
        if hi < op or hi < co:
            raise AttributeError("invalid hi value")
        if lo > op or lo > co:
            raise AttributeError("invalid lo value")
        self.op = op
        self.hi = hi
        self.lo = lo
        self.co = co

    def __str__(self):
        return '{prs: (%.3f, %.3f, %.3f, %.3f)}' % (self.op, self.hi, self.lo, self.co)

def cal(hist, td, threhold):
    if not validHist(hist, threhold) or not type(td) is float:
        return None
    lastData = hist[-1]
    if td == lastData.co:
        return None
    if (lastData.co - lastData.op) * (td - lastData.co) > 0:
        return prs(lastData.co, max(lastData.co, td), min(lastData.co, td),  td)
    firstData = hist[0]
    if (lastData.co - lastData.op) * (firstData.op - td) > 0:
        return prs(lastData.op, max(lastData.op, td), min(lastData.op, td), td)
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

p1 = prs(2.0, 5.0, 2.0, 5.0)
p2 = prs(5.0, 8.0, 5.0, 8.0)
p3 = prs(8.0, 11.0, 8.0, 11.0)

print cal([p1, p2, p3], 12.0, 3)


