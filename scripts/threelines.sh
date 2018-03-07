date=`date --date="$1" +%Y-%m-%d`
echo $date
python threeLines.py 510050 $date
