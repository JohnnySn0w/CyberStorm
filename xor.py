######################################################
# Group: Greed
# Members: Alexandra Duran Chicas, Zachary Guillot, 
# Conan Howard, Oluwatoyosi Kade, Michael Mahan, 
# Darryl Rayborn, Jonathan Ruppel, Samantha Santiago
# Date: 04/14/2018
# Program: xor.py
# Objective: Read plaintext/ciphertext from stdin, XOR
# it with the bits of a key file, and send output to 
# stdout.
######################################################

# take message of size b bytes
# take key of size b bytes
# each bit of message is XOR'd with each bit of key
# XOR: where if either message or key has 1, then resulting output is 1; otherwise 0
# plain/cipher and key must be the same byte size; otherwise, cycle it

# things to do:

# import sys commands --> done
import sys
from itertools import cycle # reference: https://docs.python.org/2/library/itertools.html

# read plain/ciphertext from stdin
for line in sys.stdin:
	characters = ''.join(line.split())
	#print characters

k = open("key", "r")
key = ''.join(k.readlines())
#print key
k.close()




# convert contents of message and key to stream of bits
# XOR the shit out of it
# convert back to characters
def xor(message, key):
	# used ^ on converted characters (converted to characters based on unicode of xor'd bytes)
	# string to hold encrypted/decrypted
	cryp = ''.join(chr(ord(a) ^ ord(b)) for (a,b) in zip(message, cycle(key)))
	print cryp


xor(characters, key)

