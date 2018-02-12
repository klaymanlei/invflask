#coding:utf-8
class hld_pu:
    date = ''
    code = ''
    name = ''
    share = 0
    cost = 0

    def to_tuple(self):
        return (self.date, self.code, self.name, self.share, self.cost)
    
    def __str__(self):
        return '{hld_pu: %s, %s, %s, %s, %s}' % (
            self.date, self.code, 
            self.name, self.share, self.cost)

    __repr__ = __str__

class trd_pu:
    date = ''
    code = ''
    name = ''
    share = 0
    prc = 0
    cst = 0

    def __str__(self):
        return '{trd_pu: %s, %s, %s, %s, %s, %s}' % (
            self.date, self.code, self.name,
            self.share, self.prc, self.cst)

    __repr__ = __str__

