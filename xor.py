######################################################
# Group: Greed
# Members: Alexandra Duran Chicas, Zachary Guillot, 
# Conan Howard, Oluwatoyosi Kade, Michael Mahan, 
# Darryl Rayborn, Jonathan Ruppel, Samantha Santiago
# Date: 04/17/2018
# Program: xor.py
# Objective: Read plaintext/ciphertext from stdin, XOR
# it with the bits of a key file, and send output to 
# stdout or to a file.
######################################################

import sys
from itertools import cycle # reference: https://docs.python.org/2/library/itertools.html (in case key is ever shorter than input, included as a "just in case" thing)
characters = '' #create blank list for the characters in the file

for line in sys.stdin:
	characters += ''.join(line) # read plain/ciphertext from stdin
characters.split()

k = open("key", "r") # opens file in read mode
key = ''.join(k.read()) # creates the list key from contents of file
key.split()
k.close() 

def xor(message, key):
	# used ^ on converted characters (sicne this is bitwise XOR operator)
	# one-liner: convert message and key into ASCII/binary, XOR them, and add the characters to a new blank list
	crypto = ''.join(chr(ord(a) ^ ord(b)) for (a,b) in zip(message, cycle(key)))
	print crypto # string to hold encrypted/decrypted text
	
xor(characters, key) # execute function
