#!/bin/sh
#Reading07
#Own implementation of the head command using awk.
#By: Andy Munch

NUM=10;

while getopts "n:" option; do
	case $option in
		n) NUM=$OPTARG ;;
		*) cat <<-EOF
			usage: head.sh
		
				-n N  Display the first N lines
			EOF
			exit 1;;
	esac
done

awk -v VALUE=$NUM 'NR <= VALUE'
