#coding:utf-8

import check_trans

trans = check_trans.load_trans('transes.txt')
print len(trans)

#dates = trans.keys();
#dates.sort()
#for date in sorted(trans.keys()):
#    print date, '\t', len(trans[date])

dates=['20170222'
    #, '20170208'
       ]
for date in dates:
    print date, trans[date]