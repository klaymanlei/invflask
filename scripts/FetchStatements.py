#coding:utf-8
import urllib2
import json
import sys
import codecs
import re
import hashlib  #MD5
import urllib  #urlencode
import time

reload(sys)
sys.setdefaultencoding( "utf-8" )

report_url = r'http://f10.eastmoney.com/NewFinanceAnalysis/MainTargetAjax'
code_list_path = 'C:/develop/workspace/stock/data/statements/'

def get(url, params):
    try:
        req_url = params is None and url or r'%s?%s' % (url, params)
        resp = urllib2.urlopen(req_url, timeout=120)
        res_str = resp.read()
        resp.close()
        return res_str
    except:
        return None

# 从get_comment接口获取realtime_click_top、big_big和loc_ab数据
def fetchComment(code, date):
    if (code[0] == '6'):
        comp_code = "SH" + code
    else:
        comp_code = "SZ" + code
    data = 'type=0&code=%s' % comp_code
    print 'parameters: ', data

    i = 0
    while i < 3:
        i += 1
        res = get(report_url, data)

        #res = '{ "errNo":201, "errMsg": "移动展示数据文件未生成"}'
        try:
            report_json = json.loads(res.encode('utf-8'))
            #print report_json
            for data in report_json:
                if data['date'] == date:
                    return '%s,财务比率,%s,每股净资产,%s' % (code,date,data['mgjzc'])
            time.sleep(0.03)
        except ValueError, e:
            print e
            if i < 3:
                time.sleep(0.03)
                continue
            else:
                return None

def read_codes(path):
    file = open(path, 'r')
    codes = []
    for line in file.readlines():
        code_str = line.split(',')[0]
        if code_str in codes:
            continue
        else:
            codes.append(code_str)
    file.close()
    return codes

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage:', sys.argv[0], '<yyyy-mm-dd>'
        exit(1)

    codes = read_codes(code_list_path + '2019-01/2019-01-01')

    # 2019-09-30、2019-06-30、2019-03-31、2018-12-31
    date = '2019-09-30'
    file = open(code_list_path + '2019-10/2019-10-01', 'w')
    cnt = 0
    for code in codes:
        cnt += 1
        print cnt, '/', len(codes)
        res = fetchComment(code, date)
        if res is None:
            continue
        file.write(res)
        file.write('\n')
        file.flush()
        time.sleep(0.03)
    file.close()