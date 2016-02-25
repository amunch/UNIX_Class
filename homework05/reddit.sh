#!/bin/sh

HEAD=10
SORT=0
SHUF=0

while getopts "rsn:" option; do
	case $option in 
		r) SHUF=1 ;;
		s) SORT=1 ;;
		n) HEAD=$OPTARG ;;
		*) echo "usage: reddit.sh [-r -s -n N] subreddits"; exit 1 ;;
	esac
done

shift $(($OPTIND - 1))

if [ "$1" = "" ]; then
	echo "No subreddits specified."
	echo "usage: reddit.sh [-r -s -n N] subreddits"
	exit 1
fi


while [ "$1" != "" ]; do
	if [ $SORT -eq "1" ]; then
		curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep url | cut -d '"' -f4 | sort | head -n $HEAD
	elif [ $SHUF -eq "1" ]; then
		curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep url | cut -d '"' -f4 | shuf | head -n $HEAD
	else
		curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep url | cut -d '"' -f4 | head -n $HEAD
	fi

	shift
done 

exit 0
