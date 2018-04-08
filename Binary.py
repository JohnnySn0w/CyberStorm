###########################################################################################
# Name: Samantha Santiago
# Date: 03/15/2018
# Description: This program will be able to decode binary-encoded messages with input
# provided from stdin. The decoded message will display on stdout. Printable characters
# and whitespace are the expected outputs, as they are ASCII characters.
###########################################################################################

# Objectives:
# read encoded message from stdin
# send output to stdout 
# detect whether input is 7 or 8-bit ASCII 
# output: printable characters and whitespace 

import sys

characters = 0

# program takes stdin here and changes it to a string. It also takes a count of total characters.
for line in sys.stdin:
        charac = ''.join(line.split()) # string of what's in the file
        characters += sum(len(chara) for chara in charac) # integer needed for mod check

# functions that take the string of binary and decodes it by converting to ASCII 
def is_seven(str, len_seven=7):
        input_str = [charac[i:i+len_seven] for i in range(0,len(charac),len_seven)]
        return ''.join([chr(int(c,base=2)) for c in input_str])
def is_eight(str, len_eight=8):
        input_str = [charac[i:i+len_eight] for i in range(0,len(charac),len_eight)]
        return ''.join([chr(int(c,base=2)) for c in input_str])

# mod functions. They determine which function shoudl be used to decode the binary string.
if (characters % 7 == 0 and characters % 8 == 0):
        print "Decoded message attempt: " + is_eight(charac)
        print "Decoded message attempt: " + is_seven(charac)

elif (characters % 8 == 0):
        print "Decoded message: " + is_eight(charac)
        
elif (characters % 7 == 0):
        print "Decoded message: " + is_seven(charac)
else:
        break


        
        
