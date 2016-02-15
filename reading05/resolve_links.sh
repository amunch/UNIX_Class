#!/bin/sh

cd $1

for i in `ls`; do
	if [ -L $i ];  then
		echo "$i links to `readlink -f $i`"
	fi  
done
