#!/bin/sh
#Uses the du command to list the sizes of all directories recursively in human
#readable form.  Use the -a command to also see files.
#By: Andy Munch
#Collaborated with Mark Pruitt

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

if [ "$1" = "" ]; then
	echo "No directory specified."
	echo "usage: disk_usage.sh [-a -n N] directory"
	exit 1
fi

while [ "$1" != "" ]; do
	if [ $FILES -eq "1" ]; then
		du -a -h $1 2> /dev/null | sort -rh | head -n $HEAD 
	else 	
		du -h $1 2> /dev/null | sort -rh | head -n $HEAD 
	fi
	
	shift
done 

exit 0	
