# coding:utf-8

import utils_db

def query(date):
    sql = 'select code,sum(amount) from t_transaction where dt=\'%s\' group by dt,code;' % date
    rows = utils_db.query(sql)
    trans = {}
    for row in rows:
        trans[row[0]] = float(row[1])
    return trans

i = 0
trans = {}
file = open('transes.txt', 'r')
for line in file:
    data = line.strip().split("\t")
    # 币种	证券名称	成交日期	成交价格	成交数量	发生金额	资金余额	剩余数量	合同编号	业务名称	手续费	印花税	过户费	结算费	证券代码	股东代码
    if (data[9] == '保证金产品赎回(天添利)'
            or data[9] == '保证金产品申购(天添利)'
            or data[9] == '赎回到帐(天添利)'):
        continue
    i += 1
    code = (data[14] == '880013' or data[14] == '---') and '-' or data[14]
    date = data[2]
    cost = float(data[5])
    tran = trans.get(date)
    if tran is None:
        tran = {}
    amount = tran.get(code)
    if amount is None:
        amount = 0
    amount += cost
    tran[code] = amount
    trans[date] = tran
    #print date, code, cost, data[9]
file.close()

print len(trans)
for (date, tran) in trans.items():
    db_trans = query(date)
    if len(db_trans) <> len(tran):
        print date
        print 'db_trans: ', db_trans
        print 'trans: ', tran
        continue
    for (code, amount) in tran.items():
        if db_trans.get(code) == None or amount - db_trans[code] > 0.0001:
            print date
            print 'trans: ', code, amount
            print 'db_trans: ', code, db_trans.get(code)
            print 'diff: ', db_trans.get(code) == None and amount or amount - db_trans[code]
