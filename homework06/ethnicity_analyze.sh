#!/bin/sh

for year in 2013 2014 2015 2016 2017 2018
do
	awk -v year=$year 'BEGIN {FS = ","} {ethnicity[$(2*year - 4024)]++} END {print year"\t"ethnicity["C"]"\t"ethnicity["O"]"\t"ethnicity["S"]"\t"ethnicity["B"]"\t"ethnicity["N"]"\t"ethnicity["T"]"\t"ethnicity["U"]}' demographics.csv 
done
