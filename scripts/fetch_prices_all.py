# coding:utf-8
import urllib2
import datetime
import sys
import time

sep = ','
api = u'http://hq.sinajs.cn/list=%s'
list_path = '../data/stock_list.txt'
out_path = '../data/'
script_name = 'fetch_prices_all.py'

def write_file(file_path, outlines):
    file_out = open(file_path, 'w')
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
    if not '"' in line or not '=' in line:
        return
    data = line.split('"', -1)
    #code = line.split('=')[0][-6:]
    code = line.split('=')[0].split('_str_')[1]
    row.append(code)
    row.append(data[1])
    out_lines.append(sep.join(row))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage:', sys.argv[0], 'code_list out_path'
        exit(1)

    out_path = sys.argv[2]
    list_path = sys.argv[1]
    script_path = sys.argv[0]
    list = read_list(script_path[:-len(script_name)] + list_path)
    tmp_list = []

    out_lines = []
    for code in list:
        tmp_list.append(code)
        if (len(tmp_list) >= 10):
            html = send_get(api, tmp_list)
            for line in html.split(';'):
                parse_line(line, out_lines)
            tmp_list = []
            time.sleep(0.5)

    html = send_get(api, tmp_list)
    for line in html.split(';'):
        parse_line(line, out_lines)
    tmp_list = []

    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    file_out = out_path + '/' + date_str
    print file_out
    write_file(file_out, out_lines)
