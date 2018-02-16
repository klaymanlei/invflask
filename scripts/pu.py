#coding:utf-8
class hld_pu:
    date = ''
    portfolio = '-'
    code = '-'
    name = '-'
    share = 0.0
    cost = 0.0

    def to_tuple(self):
        return (self.date, self.portfolio, self.code, 
            self.name, self.share, self.cost)
    
    def __str__(self):
        return '{hld_pu: %s, %s, %s, %s, %f, %f}' % (
            self.date, self.portfolio, self.code, 
            self.name, self.share, self.cost)

    __repr__ = __str__

class trd_pu:
    date = ''
    code = '-'
    name = '-'
    portfolio = '-'
    op = '-'
    share = 0.0
    prc = 0.0
    cst = 0.0

    def __str__(self):
        return '{trd_pu: %s, %s, %s, %s, %s, %f, %f, %f}' % (
            self.date, self.code, self.name, self.portfolio,
            self.op, self.share, self.prc, self.cst)

    __repr__ = __str__

class ast_pu:
    date = ''
    portfolio = '-'
    code = '-'
    name = '-'
    type = '-'
    share = 0.0
    prc = 0.0

    def to_tuple(self):
        return (self.date, self.portfolio, self.code, self.name, self.type, self.share, self.prc)

    def __str__(self):
        return '{ast_pu: %s, %s, %s, %s, %s, %f, %f}' % (
            self.date, self.portfolio, self.code, self.name, 
            self.type, self.share, self.prc)

    __repr__ = __str__

