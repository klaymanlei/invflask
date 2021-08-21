#coding:utf-8
#import urllib.request
import json
import sys
import codecs
import re
import hashlib  #MD5
import urllib  #urlencode
import time
import importlib

importlib.reload(sys)
# sys.setdefaultencoding( "utf-8" )

report_url = r'http://f10.eastmoney.com/NewFinanceAnalysis/MainTargetAjax'
code_list_path = 'D:/dev/projects/invflask/data/statements/'
# http://f10.eastmoney.com/NewFinanceAnalysis/zcfzbAjax?companyType=4&reportDateType=0&reportType=1&endDate=&code=SH601668
# http://f10.eastmoney.com/NewFinanceAnalysis/lrbAjax?companyType=4&reportDateType=0&reportType=1&endDate=&code=SH601668
# http://f10.eastmoney.com/NewFinanceAnalysis/xjllbAjax?companyType=4&reportDateType=0&reportType=1&endDate=&code=SH601668

def get(url, params):
    try:
        req_url = params is None and url or r'%s?%s' % (url, params)
        resp = urllib.request.urlopen(req_url, timeout=120)
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
    print('parameters: ', data)

    i = 0
    while i < 3:
        i += 1
        res = get(report_url, data)

        #res = '{ "errNo":201, "errMsg": "移动展示数据文件未生成"}'
        try:
            #report_json = json.loads(res.encode('utf-8'))
            report_json = json.loads(res)
            #print report_json
            for data1 in report_json:
                if data1['date'] == date:
                    return '%s,财务比率,%s,每股净资产,%s' % (code, date, data1['mgjzc'])
            time.sleep(0.03)
        except ValueError as e:
            print(e)
            if i < 3:
                time.sleep(0.03)
                continue
            else:
                return None
        except TypeError as e:
            print(e)
            print(report_url, data)
            print(res)
            exit(255)

def read_codes(path):
    file = open(path, 'r', encoding='utf-8')
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
        print('Usage:', sys.argv[0], '<yyyy-mm-dd>')
        exit(1)

    codes = read_codes(code_list_path + '2019-01/2019-01-01')

    # 2019-09-30、2019-06-30、2019-03-31、2018-12-31
    #date_map = {"":""}
    date = '2021-03-31'
    file = open(code_list_path + '2021-04/2021-04-01', 'w')
    cnt = 0
    for code in codes:
        cnt += 1
        print(cnt, '/', len(codes))
        res = fetchComment(code, date)
        if res is None:
            continue
        file.write(res)
        file.write('\n')
        file.flush()
        time.sleep(0.03)
    file.close()