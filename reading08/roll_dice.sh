#!/bin/sh
#Reading08
#Simulates random dice rolls using the shuf command.
#By: Andy Munch

ROLLS=10;
SIDES=6;

while getopts "r:s:" option; do
	case $option in
		r) ROLLS=$OPTARG ;;
		s) SIDES=$OPTARG ;;
		*) cat <<-EOF
			usage: roll_dice.sh [-r ROLLS -s sides]

			     -r ROLLS        Number of rolls of die (default: 10)
			     -s SIDES        Number of sides on die (default: 6)
			EOF
			exit 1;;
	esac
done

for ((num=0;num<$ROLLS;num++)); do
	shuf -i 1-$SIDES -n 1
done
