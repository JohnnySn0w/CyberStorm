from datetime import datetime
import time
from time import mktime
import hashlib
import sys

letters = ""
numbers = ""
result = ""
epoch = str(sys.stdin.readline()).strip().split()
now = "2013 05 06 07 43 25".split()
#Note: both epoch and current times are converted to utc to account for daylight savings  
#convert epoch time to POSIX then to utc
epoch_time = datetime.utcfromtimestamp(time.mktime(datetime(int(epoch[0]), int(epoch[1]), int(epoch[2]), int(epoch[3]), int(epoch[4]), int(epoch[5])).timetuple()))

#current utc time
#now = datetime.utcnow().replace(microsecond=0)
now_time = datetime.utcfromtimestamp(time.mktime(datetime(int(now[0]), int(now[1]), int(now[2]), int(now[3]), int(now[4]), int(now[5])).timetuple()))

#subtract epoch time from current then convert to POSIX
delta_time = int((now_time - epoch_time).total_seconds())

#first md5 hash conversion
hash_time = hashlib.md5(bytes(delta_time)).hexdigest()

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

#print(str(now_time))
#print(str(epoch_time))
#print(delta_time)
#print(double_hash_time)
print(result)
~                                                                                                                                                                                                                                                                               
~                           
