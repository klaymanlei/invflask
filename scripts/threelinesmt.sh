#!/bin/bash

if [ $# -ne 2 ]
then
        echo "Usage: $0 <yyyymmdd> <code>"
        exit 255
fi

date=`date --date="$1" +%Y-%m-%d`
echo $date
python /home/hadoop/python/vflask/invflask/scripts/threeLinesMt.py $2 $date
