#coding:utf-8

class holding:
    date = ''
    portfolio = '-'
    code = '-'
    sec_type = '-'
    quantity = 0.0
    amount = 0.0

    def to_tuple(self):
        return (self.date, self.portfolio, self.code, self.sec_type,
                float(self.quantity), float(self.amount))

    def to_str_tuple(self):
        return (self.date, self.portfolio, self.code, self.sec_type,
                str(self.quantity), str(self.amount))

    def __str__(self):
        return '{holding: %s, %s, %s, %s, %f, %f}' % (
            self.date, self.portfolio, self.code, self.sec_type,
            self.quantity, self.amount)

    __repr__ = __str__

class transaction:
    date = ''
    code = '-'
    operation = '-'
    portfolio = '-'
    sec_type = '-'
    quantity = 0.0
    price = 0.0
    tax = 0.0
    other_charges = 0.0
    amount = 0.0

    def __str__(self):
        return '{transaction: %s, %s, %s, %s, %s, %f, %f, %f, %f, %f}' % (
            self.date, self.code, self.operation, self.portfolio,
            self.sec_type, self.quantity, self.price, self.tax, self.other_charges, self.amount)

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

