#!/bin/bash
FILE=$1
if [ -f $FILE ]
then
path_to_file=$FILE
elif [ ! -f $FILE ] 
then 
echo "Нет такого файла: $FILE" 
exit 1
elif [ ! -n $FILE ]
then
path_to_file=$(ls *.log)
fi
grep "POST\|GET" $path_to_file | wc -l > result && echo "ok" || echo 'fail'
echo '===' >> result
grep "POST" $path_to_file | wc -l >> result && echo "ok" || echo 'fail'
echo '===' >> result
grep "GET" $path_to_file | wc -l >> result && echo "ok" || echo 'fail'
echo '===' >> result
cat $path_to_file | sort -r -nk10 | awk '{ print $7 " " $9}' | uniq -c | head -10  >> result && echo "ok" || echo 'fail'
echo '===' >> result
cat $path_to_file | awk '$9 ~ /40[0-9]/ {print $0}' | sort -rk7 -k9 | awk '{ print $7 " " $9 }'| uniq -c | sort -rnk1 | head -n10 >> result && echo "ok" || echo 'fail'
echo '===' >> result
cat $path_to_file | awk '$9 ~ /50[0-9]/ {print $0}' | sort -nrk 10 | awk '{ print $7 " " $9}' | head -n10 >> result && echo "ok" || echo 'fail'
echo '===' >> result