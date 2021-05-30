#!/bin/bash
source ~/.bash_profile

mydate=`date +%Y%m%d`
mydate_formate=`date +%Y-%m-%d`

python /home/hadoop/dev/workspace/vflask/project/invflask/scripts/fetch_prices_all.py ../data/futures_list.txt /home/hadoop/data/futuresdata

echo "hdfs dfs -mkdir -p /invest/ods/ods_futures_price_sina_hqapi/${mydate}/"
hdfs dfs -rm -r /invest/ods/ods_futures_price_sina_hqapi/${mydate}/
hdfs dfs -mkdir -p /invest/ods/ods_futures_price_sina_hqapi/${mydate}/

echo "hdfs dfs -put /home/hadoop/data/futuresdata/${mydate_formate} /invest/ods/ods_futures_price_sina_hqapi/${mydate}/"
hdfs dfs -put /home/hadoop/data/futuresdata/${mydate_formate} /invest/ods/ods_futures_price_sina_hqapi/${mydate}/

echo "alter table ods_futures_price_sina_hqapi add if not exists partition (dt='${mydate}') location '/invest/ods/ods_futures_price_sina_hqapi/${mydate}/';"
hive -e "alter table ods_futures_price_sina_hqapi add if not exists partition (dt='${mydate}') location '/invest/ods/ods_futures_price_sina_hqapi/${mydate}/';"
