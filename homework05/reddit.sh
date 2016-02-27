#!/bin/sh
#Displays the links for a subreddit, and sorts or shuffles them depending on the user's input.
#By: Andy Munch

HEAD=10
CHOICE=0

while getopts "rsn:" option; do
	case $option in 
		r) CHOICE=1 ;;
		s) CHOICE=2 ;;
		n) HEAD=$OPTARG ;;
		*) cat <<-EOF
			usage: reddit.sh [options] subreddits...

				-r      Shuffle the links
				-s      Sort the links	
				-n N    Number of links to display (default is 10)
			EOF
			exit 1 ;;
	esac
done

shift $(($OPTIND - 1))

if [ "$1" = "" ]; then
	cat <<-EOF
		usage: reddit.sh [options] subreddits...

			-r      Shuffle the links
			-s      Sort the links  
			-n N    Number of links to display (default is 10)
		EOF
	exit 1
fi


while [ "$1" != "" ]; do
	if [ $CHOICE -eq "2" ]; then
		curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep url | grep -v redditmedia | cut -d '"' -f4 | grep -v '&lt' | grep -v embed | sort | head -n $HEAD
	elif [ $CHOICE -eq "1" ]; then
		curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep url | grep -v redditmedia | cut -d '"' -f4 | shuf | grep -v '&lt' | grep -v embed | head -n $HEAD
	else
		curl -s http://www.reddit.com/r/$1/.json | python -m json.tool | grep url | grep -v redditmedia | cut -d '"' -f4 | grep -v '&lt' | grep -v embed | head -n $HEAD
	fi

	shift
done 

exit 0
