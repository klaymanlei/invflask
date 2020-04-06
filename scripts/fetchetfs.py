#coding:utf-8
import urllib2
import datetime

def write_file(file_path, outlines):
    file_out = open(file_path, 'a')
    for line in outlines:
        if len(line.strip()) > 0:
            file_out.write(line)
            file_out.write('\n')
    file_out.close()

def get_season(date_str):
    strs = date_str.split('-')
    if len(strs) != 3:
        return date_str
    mon = int(strs[1])
    season_mon = mon - (mon + 2) % 3
    return "%s-%02d-01" % (strs[0], season_mon)

#url = 'http://finance.sina.com.cn/fund/quotes/510050/bc.shtml'
#url = 'http://hq.sinajs.cn/list=sz150019'
sep = ','
list = ['sz159915', 'sh510050', 'sz150019', 'sh510500', 'sz399967', 'sz399975', 'sh518800', 'sz399395']
url = 'http://hq.sinajs.cn/list=%s' % sep.join(list)
page = urllib2.urlopen(url)
html = page.read().decode('gbk').encode('utf-8')
page.close()

rownum = 0
outlines = []
for line in html.split(';'):
    row = []
    if len(line.strip()) == 0:
        continue
    data = line[line.find('"') + 1 : -1].strip().strip(',').split(',')
    row.append(list[rownum][2:])
    row.append(data[-3])
    row.append(data[1])
    row.append(data[4])
    row.append(data[5])
    row.append(data[3])
    row.append(data[8])
    row.append(data[3])
    outlines.append(sep.join(row))
    rownum += 1

date_str = datetime.datetime.now().strftime('%Y-%m-%d')
file_out = '/home/hadoop/data/seasondata/%s' % get_season(date_str)
# file_out = './%s' % get_season(date_str)
write_file(file_out, outlines)
