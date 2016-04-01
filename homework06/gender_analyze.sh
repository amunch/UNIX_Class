#!/bin/sh

for year in 2013 2014 2015 2016 2017 2018
do
	awk -v year=$year 'BEGIN {FS = ","} {gender[$(2*year - 4025)]++} END {print year"\t"gender["M"]"\t"gender["F"]}' demographics.csv 
done
