#!/bin/sh
#Displays a special message after SIGHUP is received, taunts if SIGINT OR 
#SIGTERM is received, and a witty message if no signals after 10 seconds.
#Homework 4 Activity 03
#By: Andy Munch
#Collaborated with Mark Pruitt
 
password() {
/afs/nd.edu/user15/pbui/pub/bin/cowsay -d -f head-in <<-EOF
	Hmm... I recognize you $(whoami)...
	Take this password. You will need it. 
	The password is skjdbgksbglihrbfljber.
	EOF
exit
}
 
taunt() {
/afs/nd.edu/user15/pbui/pub/bin/cowsay -d -f head-in <<-EOF
	Hey, $(whoami).
	Get your head out of your ass!
	EOF

exit
}
 

NUM=10
IT=0

/afs/nd.edu/user15/pbui/pub/bin/cowsay -d -f head-in "Uh... What? What do you want"

while [ $IT -lt $NUM ]; do
	sleep 1
	IT=$((IT+1))
	trap password SIGHUP
	trap taunt SIGINT
	trap taunt SIGTERM
done

/afs/nd.edu/user15/pbui/pub/bin/cowsay -d -f head-in "Ugh... I'm going back to sleep... ZzZzZ.."
