#!/usr/bin/env python3

######################################################
# Group: Greed
# Members: Alexandra Duran Chicas, Zachary Guillot, 
# Conan Howard, Oluwatoyosi Kade, Michael Mahan, 
# Darryl Rayborn, Jonathan Ruppel, Samantha Santiago
# Date: 04/26/2018
# Program: timelock.py
# Objective: Implement the following timelock algorithm:
# calculate the time seconds elapsed of the current 
# system time since an epoch time, compute the 
# MD5(MD5(time elapsed)), extract and concatenate the
# first two letters of the hash from left-to-right 
# followed by the first two single-digit integers of the
# hash from right-to-left, and output this "code" with
# each one being valid for 60 seconds 
#####################################################

import sys
import time
import hashlib
from time import mktime 
from datetime import datetime

letters = ""
numbers = ""
result = ""
#read the epoch from stdin 
epoch = str(sys.stdin.readline()).strip().split()

#Note: both epoch and current times are converted to utc to account for daylight savings
#Also, both epoch and current times are formatted YYYY MM DD HH mm SS

#epoch time is converted to POSIX then to utc time
epoch_time = datetime.utcfromtimestamp(time.mktime(datetime(int(epoch[0]), int(epoch[1]), int(epoch[2]), int(epoch[3]), int(epoch[4]), int(epoch[5])).timetuple()))

#current utc time without microseconds
now = datetime.utcnow().replace(microsecond=0)

#calculate time elapsed by subtracting epoch time from current then convert to POSIX
delta_time = (now - epoch_time).total_seconds()

#change time elapsed such that each new code is valid for 60 seconds
interval = delta_time % 60
delta_time -= interval

#first md5 hash conversion
hash_time = hashlib.md5(str(delta_time).encode()).hexdigest()
#second md5 hash conversion
double_hash_time = hashlib.md5(hash_time.encode()).hexdigest()

#extract all letters [a-f] of double hash (from left-to-right)
for l in double_hash_time:
    if l.isalpha() is True:
        letters += l
#remove any letters beyond the first two
letters = letters[:2]

#extract all one-digit integers [0-9] of double hash (from left-to-right)
for n in double_hash_time:
    if n.isdigit() is True:
        numbers += n
#reverse the numbers in the hash so it's read from right-to-left
reversed_numbers = numbers[::-1]
#remove any numbers beyond the first two
numbers = reversed_numbers[:2]

#concatenate letters and numbers
result = letters + numbers

#send the 4-character code stdout
print(result)
