#!/bin/sh
#Reading08
#Simulates 1000 dice rolls.
#By: Andy Munch

roll_dice.sh -r 1000 | awk '{num[$1] += 1} END {for (number in num) {print number"\t"num[number]}}' | sort

