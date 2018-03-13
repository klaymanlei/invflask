#!/bin/bash

if [ $# -ne 3 ]
then 
	echo "Usage: $0 <start_date yyyymmdd> <end_date yyyymmdd> <sh>"
	exit 255
fi

date="$1"

while (("$date"<="$2"))
do
    echo "$3 $date"
    rs=`$3 $date`
    date=`date --date="$date +1day" +%Y%m%d`
done
