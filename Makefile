SHELL := /bin/bash

#wep stuff
wep:
	echo "\n4 terminals, init(terminal 1), input vars(manually in terminals 1-3),  \n"

wepInit:
	ifconfig | grep 'wl'




wepMakeMon:
	sudo airmon-ng start $int $chan
wepListenMon:
	sudo airodump-ng -c $chan --bssid $bssid -w output mon0

#wpa stuff
wpa:
	echo "\ninit, \n"

wpa2Init:

#general use
wanScan:
	sudo iwlist $int scan | grep -E '(Address:|Channel:|ESSID:)'

stopNetworkMan:
	sudo /etc/init.d/network-manager stop
	sudo ifconfig $int down
