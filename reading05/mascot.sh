#!/bin/sh

name=`uname`

case $name in
	Linux ) echo "Tux"
		;;
	Darwin ) echo "Hexley"
		;;
	*BSD ) echo "Beastie"
		;;
	* ) echo "Maching not recognized."
		;;
esac	
