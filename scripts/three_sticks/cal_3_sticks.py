#encoding=utf-8
#!/usr/bin/python

import sys
import os
import codecs
from datetime import datetime, timedelta

from db_utils import *

# 从文本文件中读取当日价格
def load(filepath, date, code):
    exist = os.path.exists(filepath)
    if not exist:
        print "数据文件不存在"
        exit(255)
    file = codecs.open(filepath, 'r', 'utf-8')

    rs = {}
    for line in file:
        line = file.readline().split('\t')
        date_read = line[0].strip()
        code_read = line[1].strip()
        if date != date_read or code != code_read:
            continue
        rs['date'] = date_read
        rs['code'] = code_read
        rs['open'] = float(line[2].strip())
        rs['close'] = float(line[3].strip())
        break

    if len(rs) == 0:
        print "未发现当日数据"
        exit(255)

    return rs

# 计算趋势延续或反转的门槛，hist要求按时间倒序排列
def threhold(hist):
    forward = -1    # 趋势延续的门槛
    backward = -1   # 趋势反转的门槛
    if len(hist) > 0:
        data = hist[0]  # 首先计算最新一条历史记录的方向（hist按倒序排列）
        forward = float(data['close'])
        backward = float(data['open'])
        for i in range(1, len(hist)):
            if same_direct(backward, forward, float(hist[i]['open']), float(hist[i]['close'])):
                backward = float(hist[i]['open'])
            else:
                break
    #print (forward, backward)
    return (forward, backward)

# 判断当前K线方向和历史K线方向是否相同, 返回结果true代表方向相同，false代表方向相反
def same_direct(curr_open, curr_close, hist_open, hist_close):
    curr_direct = curr_close - curr_open  # 用current_direct的正负号代表当前趋势方向
    hist_direct = hist_close - hist_open  # 用hist_direct的正负号代表历史趋势方向
    # current_direct与hist_direct乘积大于0代表方向相同，小于0代表方向相反
    return curr_direct * hist_direct > 0

# 判断当前日期与指定日期是否同一周, 输入参数均为yyyy-mm-dd格式
def get_clean_date(date, type):
    # 默认删除当日数据
    clean_date = date
    last_data = get_hist(date, code, type, 1)
    if type != 'day' and len(last_data) > 0:
        last_date = last_data[0]['date']
        curr = datetime.strptime(date, '%Y-%m-%d')
        hist = datetime.strptime(last_date, '%Y-%m-%d')

        print datetime(curr.year, curr.month, 1)
        print datetime(hist.year, hist.month, 1)

        if type == 'week':
            # 如果最后一天和当日属于同一周，则删除本周已有的数据
            if curr.strftime('%W') == hist.strftime('%W'):
                clean_date = datetime.strftime(curr - timedelta(days=curr.weekday()), '%Y-%m-%d')
        elif type == 'month':
            if datetime(curr.year, curr.month, 1) == datetime(hist.year, hist.month, 1):
                clean_date = datetime.strftime(datetime(curr.year, curr.month, 1), '%Y-%m-%d')
        else:
            print '类型参数仅支持 day|week|month'
            exit(255)
    return clean_date

if __name__ == '__main__':
    # 参数检查：date，code，type，inputpath
    if len(sys.argv) != 5:
        print "Usage: %s [yyyy-mm-dd] [code] [type] [input_path]" % (sys.argv[0])
        exit(-1)
    else:
        date = sys.argv[1]
        code = sys.argv[2]
        type = sys.argv[3]
        filepath = sys.argv[4]

    # 清理需要覆盖的历史数据
    clean_date = get_clean_date(date, type)
    # 根据计算的clean date清理需要覆盖的数据
    clean_after(clean_date, code, type)

    # 天和周K线计算3线反转，月K线计算2线反转
    stick_cnt = 3
    if type == 'month':
        stick_cnt = 2

    # 读取最新一天的记录
    data = load(filepath, date, code)
    print 'current:', data

    # 查询最近的stick_cnt条历史记录
    hist = get_hist(date, code, type, stick_cnt)
    print 'hist:'
    for hist_data in hist:
        print hist_data

    # 计算趋势延续及反转的门槛
    (forward, backward) = threhold(hist)
    print 'threhold:'
    print forward, backward

    if same_direct(forward, data['close'], backward, forward):
        # 如果最新的close价格相对趋势延伸阈值的方向与历史K线方向一致，则趋势延伸
        print '趋势延伸'
        #insert(date, code, type, forward, data['close'])
    elif not same_direct(backward, data['close'], backward, forward):
        # 如果最新的close价格相对趋势反转阈值的方向与历史K线方向相反，则趋势反转
        print '趋势反转'
        #insert(date, code, type, backward, data['close'])
    else:
        # 如果最新的close价格相对趋势延伸阈值的方向与历史K线方向相反，且相对趋势反转阈值的方向与历史K线方向相同，则最新的close价格落在两个阈值之间，趋势不更新
        print '不更新'

    print 'done'

