#coding:utf-8
import datetime
import time

DB_SERVER = '192.168.1.199'
DB_PORT = 3306
DB_USER = 'invest'
DB_PW = 'InvestNPass4!'
DB = 'invest'

#DB_SERVER = '10.88.15.50'
#DB_PORT = 23306
#DB_USER = 'leidayu'
#DB_PW = 'leidayu'
#DB = 'invdb'

TODAY = time.strftime('%Y-%m-%d',time.localtime(time.time())) 
