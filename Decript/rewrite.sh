#! /bin/bash
[ -z "$3" ] && echo "you need input one file" && exit 0
t1=`cut $1 -d' ' -f 1`
t2=`cut $1 -d' ' -f 6`
t3=`cut $1 -d' ' -f 11`
t4=`cut $1 -d' ' -f 16`
T=${t1}${t2}${t3}${t4}
echo "$T" > tmp

s1=`cut $1 -d' ' -f 3`
s2=`cut $1 -d' ' -f 8`
s3=`cut $1 -d' ' -f 13`
s4=`cut $1 -d' ' -f 18`
S=${s1}${s2}${s3}${s4}
echo "$S" > tmp1
#echo "$T$S"

n=`cat $2 | wc -l`
for((i=1;i<=n;i++))
do
	head -n $i $2 | tail -n 1 >> output.txt
	echo -e ":'\c" >> output.txt
	head -n $i $3 | tail -n 1 >> output.txt
	echo -e "',\c" >> output.txt
done
