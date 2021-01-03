# coding:utf-8
import urllib2
import datetime
import sys
import time

sep = ','
api = u'http://hq.sinajs.cn/list=%s'
list_path = '../data/stock_list.txt'
out_path = '../data/'


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

def send_get(api, list):
    url = api % sep.join(list)
    print url
    for j in range(1, 4):
        try:
            resp = urllib2.urlopen(url, timeout=120)
            html = resp.read().decode('gbk').encode('utf-8')
            break
        except:
            resp = None
    resp.close()
    return html

def read_list(path):
    list = []
    try:
        file = open(path, 'r')
        for line in file:
            code = line.split('\t')
            if len(code) > 1:
                list.append(code[0])
    except:
        print 'load stock list fail'
    return list

def parse_line(line, out_lines):
    row = []
    if len(line.strip()) == 0:
        return
    data = line[line.find('"') + 1: -1].strip().strip(',').split(',')
    row.append(list[rownum][2:])
    row.append(data[-3])
    row.append(data[1])
    row.append(data[4])
    row.append(data[5])
    row.append(data[3])
    row.append(data[8])
    row.append(data[3])
    out_lines.append(sep.join(row))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage:', sys.argv[0], 'out_path'
        exit(1)

    out_path = sys.argv[1]
    list = read_list(list_path)
    tmp_list = []

    out_lines = []
    for code in list:
        tmp_list.append(code)
        if (len(tmp_list) >= 10):
            html = send_get(api, tmp_list)
            for line in html.split(';'):
                parse_line(line, out_lines)
            tmp_list = []
            time.sleep(1)

    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    file_out = out_path + '/' + get_season(date_str)
    print file_out
    write_file(file_out, out_lines)
