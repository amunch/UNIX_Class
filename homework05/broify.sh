#!/bin/sh

DELIM="#"
STRIP='1'

while getopts "d:W" option; do
	case $option in
		d) DELIM=$OPTARG ;;
		W) STRIP=0 ;;
		*) cat <<-EOF
			usage: broify.sh
			
				-d DELIM   Use this as the comment delimiter.
				-W         Don't strip empty line.
			EOF
			exit 1 ;;
	esac
done 

if [ $STRIP -eq '1' ]; then
	sed -r "s|$DELIM.*||g" | sed 's/[ \t]*$//' | sed '/^$/d'
else
	sed -r "s|$DELIM.*||g" | sed 's/[ \t]*$//'
fi
