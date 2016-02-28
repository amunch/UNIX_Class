#!/bin/sh
#Reading07
#Uses awk to parse the contents of the CCL Catalog Server
#By: Andy Munch

URL=${1:-http://catalog.cse.nd.edu:9097/query.text}

curl -s $URL | awk '/cpus/ {count = count + $2} END{print "Total CPUs: " count}'
curl -s $URL | awk '/name/ {array[$2]++} END{for (key in array) count++} END{print "Total Machines: " count}'
curl -s $URL | awk '/type/ {array[$2]++} END{largest=0; for(key in array) if(array[key]>largest) {type=key; largest=array[key];}} END{print "Most Prolific Type: " type}'

