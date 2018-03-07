#!/bin/bash

if [ $# -ne 3 ]
then 
	echo "Usage: $0 <start_date yyyymmdd> <end_date yyyymmdd> <sh>"
	exit 255
fi

start_date=`date --date="$1" +%Y%m%d`
end_date=`date --date="$2" +%Y%m%d`

while (("$start_date"<="$end_date"))
do
    echo "$3 $start_date"
    rs=`$3 $start_date`
    start_date=`date --date="$start_date +1day" +%Y%m%d`
done
