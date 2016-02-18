#!/bin/sh

FILES=0
HEAD=10

while getopts "an:" option; do
	case $option in
		a) FILES=1 ;;
		n) HEAD=$OPTARG ;;
		*) echo "usage: disk_usage.sh [-a -n N] directory"; exit 1 ;;
	esac
done 

shift $(($OPTIND - 1))

echo $FILES

if [ $FILES -eq "1" ]; then
	du -a -h $1 | sort -rn | head -n $HEAD
else 	
	du -h $1 | sort -rn | head -n $HEAD
fi

exit 0	
