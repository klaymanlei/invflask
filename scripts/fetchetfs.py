#coding:utf-8
import urllib2

#url = 'http://finance.sina.com.cn/fund/quotes/510050/bc.shtml'
#url = 'http://hq.sinajs.cn/list=sz150019'
sep = ','
list = ['sz159915', 'sh510050', 'sz150019', 'sh510500']
url = 'http://hq.sinajs.cn/list=%s' % sep.join(list)
page = urllib2.urlopen(url)
html = page.read().decode('gbk').encode('utf-8')
page.close()

rownum = 0
for line in html.split(';'):
    row = []
    if len(line.strip()) == 0:
        continue
    data = line[line.find('"') + 1 : -1].split(',')
    row.append(list[rownum][2:])
    row.append(data[-3])
    row.append(data[1])
    row.append(data[4])
    row.append(data[5])
    row.append(data[3])
    row.append(data[8])
    row.append(data[3])
    print sep.join(row)
    rownum += 1
    #if len(data) == 33:
    #    print data[3]

# print html.decode('gbk').encode('utf-8')
