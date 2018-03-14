#!/bin/bash

if [ $# -ne 1 ]
then
        echo "Usage: $0 <yyyymmdd>"
        exit 255
fi

date=`date --date="$1" +%Y-%m-%d`
echo $date

codes=(510050 510500 150019 159915)

for code in ${codes[@]} 
do 
	echo $code
	/home/hadoop/python/vflask/invflask/scripts/threelines.sh $date $code
done
