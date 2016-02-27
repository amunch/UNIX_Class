#!/bin/sh
#Cipher technique to encrypt and inputted message.
#By: Andy Munch
#Online resource: http://unix.stackexchange.com/questions/151654/checking-if-an-input-number-is-an-integer

NUM=13

if [ "$1" != "" ]; then
	NUM=$1
fi

if ! [ $NUM -eq $NUM ] 2> /dev/null; then
	cat <<-EOF
		usage: caesar.sh [rotation]

		This program will read from stdin and rotate (shift right) the text be the specified roation.  If none is specified, then the default value is 13.
	EOF
	exit 1
fi

NUM=`expr $NUM % 26`

lower="abcdefghijklmnopqrstuvwxyz"
UPPER="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

SET1=$UPPER$lower

SHIFTUP1=$(echo $UPPER | cut -b `expr $NUM + 1`-26)
SHIFTUP2=$(echo $UPPER | cut -b 1-$NUM)
shiftlow1=$(echo $lower | cut -b `expr $NUM + 1`-26)
shiftlow2=$(echo $lower | cut -b 1-$NUM)

SET2=$SHIFTUP1$SHIFTUP2$shiftlow1$shiftlow2

tr $SET1 $SET2
