#!/usr/bin/env python3

import os        # Used for file stat
import sys       # Used for I/O
import argparse  # Used to parse parameters

sentinel = bytes([0x0,0xff,0x0,0x0,0xff,0x0])
# Default sentinel (hard-code bytes here)
files = []
# Keep track of all opened files

parser = argparse.ArgumentParser()
method_group = parser.add_mutually_exclusive_group(required = True)  # -b or -B
action_group = parser.add_mutually_exclusive_group(required = True)  # -s or -r
# Use groups to make arguments mutually exclusive (i.e. user can only choose one)

method_group.add_argument("-b", "--bit", dest = "b", help = "Use the 'bit' method", action = "store_true")
method_group.add_argument("-B", "--byte", dest = "B", help = "Use the 'byte' method", action = "store_true")
action_group.add_argument("-s", "--store", dest = "s", help = "Store (and hide) data", action = "store_true")
action_group.add_argument("-r", "--retrieve", dest = "r", help = "Retrieve hidden data", action = "store_true")
parser.add_argument("-o", metavar = "<off>", dest = "o", help = "Set offset to <off>", type = int, default = 0)
parser.add_argument("-i", metavar = "<int>", dest = "i", help = "Set interval to <int>", type = int, default = 1)
parser.add_argument("-W", metavar = "<wra>", dest = "W", help = "Set wrapper file to <wra>", required = True)
parser.add_argument("-H", metavar = "<hid>", dest = "H", help = "Set hidden file to <hid>")
parser.add_argument("-S", metavar = "<sen>", dest = "S", help = "Change sentinel (ascii)", default = None)
# Configure arguments as specified by the assignment
# metavar and help used to make --help doc pretty
# dest is the variable name to assign to
# action = "store_true" means that dest will be set to True

args = parser.parse_args()
# Read the users given arguments and store them as such:
# args.b, args.B, args.s, args.r, args.o, args.i, args.W, args.H, args.debug

if args.S != None:
	temp = []
	for c in args.S:
		temp.append(ord(c))
	sentinel = bytes(temp)
# Check if user specified sentinel in arguments

def terminate(msg):
	print("\n" + sys.argv[0] + ": " + msg, file = sys.stderr)
	# Let the user know why the program ended
	for f in files:
		f.close()
	quit()
# Make sure all opened files are closed upon termination

def printr(h):
	sys.stdout.buffer.write(bytes([h]))
# Print as a raw byte

def fopen(file_name):
	temp = None
	try:
		temp = open(file_name)
		files.append(temp)
	except:
		terminate("error opening file " + file_name + ".")
	return temp

if args.i < 1:
	terminate("error: <int> cannot be less than 1")
	# Make sure user isnt trolling

if args.o < 0:
	terminate("error: bad <off> value")
	# Make sure user isnt trolling

args.i -= 1
# Change to number of bytes to skip (Do not change)

wrap = None
try:
	wrap = open(args.W, 'rb') #rb: read raw
	files.append(wrap)
except:
	terminate("error opening file " + args.W + "\n")
	# Make sure file to wrap is usable by program (i.e. it exists)

w_size = os.path.getsize(args.W)
# Get size of wrapper

if (args.o > w_size):
	terminate("error: offset cannot be larger than wrapper size: " + str(w_size))
	# Make sure user isnt trolling

if args.s:
	# User wants to hide a file

	if args.H == None:
		terminate("error: the following arguments are required: -H\n")
		# Cannot hide a file if user doesn't tell us what file to hide
	
	hide = None
	try:
		hide = open(args.H, 'rb')  #rb: read raw
		files.append(hide)
	except:
		terminate("error opening file " + args.H + "\n")
		# Make sure file to hide is usable by program (i.e. it exists)

	h_size = os.path.getsize(args.H)
	# Get sizes of file to hide

	if args.B and (h_size * args.i + args.o + 6) > w_size:
		terminate("Wrapper too small, must be at least " + str(h_size * args.i + args.o + 6) + " bytes")
	elif args.b and (h_size * args.i * 8 + args.o + 6 * 8) > w_size:
		terminate("Wrapper too small, must be at least " + str(h_size * args.i * 8 + args.o + 6 * 8) + " bytes")
	# Make sure given wrapper is large enough to store the hidden file inside
	
	# At this point, ready to hide file
	sys.stdout.buffer.write(wrap.read(args.o))         # Print header
	sys.stdout.flush()

	if args.B:
		# Using byte method

		for i in range(h_size):
			sys.stdout.flush()                 # flush it
			printr(ord(hide.read(1)))          # print a byte of the hidden file
			wrap.seek(wrap.tell() + 1)         # skip a byte of the wrapper
			for j in range(args.i):            # 
				printr(ord(wrap.read(1)))  # print 'i' bytes of the wrapper

		for i in range(6):
			sys.stdout.flush()                    # flush it
			printr(sentinel[i])                   # print raw byte of sentinel
			wrap.seek(wrap.tell() + 1)            # skip a byte of the wrapper
			for j in range(args.i):               # 
				printr(ord(wrap.read(1)))     # print 'i' bytes of the wrapper
		
		next_byte = wrap.read(1)                   #
		while next_byte != b'':                    #
			sys.stdout.flush()                 #
			printr(ord(next_byte))             #
			next_byte = wrap.read(1)           # print the rest of the wrapper
	else:
		# Using bit method

		for i in range(h_size):                           #
			sys.stdout.flush()                        # Flush it
			h = ord(hide.read(1))                     # Get next byte to hide
			for j in range(8):                        # 
				w = ord(wrap.read(1))             # ^ Read next wrapper byte
				w &= 0b11111110                   # ^ Set LSB to 0
				w |= ((h & 0b10000000) >> 7)      # ^ Shift MSB of h to LSB of w
				printr(w)                         # ^ Print raw byte
				h <<= 1                           # ^ Shift in next byte of h
				sys.stdout.buffer.write(wrap.read(args.i)) # Skip interval
				sys.stdout.flush()

		for i in range(6):                                #
			sys.stdout.flush()                        # Flush it
			h = sentinel[i]                           # Get next byte of sentinel
			for j in range(8):                        # 
				w = ord(wrap.read(1))             # ^
				w &= 0b11111110                   # ^
				w |= ((h & 0b10000000) >> 7)      # ^
				printr(w)                         # ^
				h <<= 1                           # ^
				sys.stdout.buffer.write(wrap.read(args.i)) # Skip interval
				sys.stdout.flush()
		
		next_byte = wrap.read(1)                   #
		while next_byte != b'':                    #
			sys.stdout.flush()                 #
			printr(ord(next_byte))             #
			next_byte = wrap.read(1)           # print the rest of the wrapper

else:
	# User wants to retrieve hidden file

	wrap.seek(args.o)  # Skip header

	if args.B:
		# Using Byte method

		next_byte = wrap.read(1)                                           # Retrieve byte
		done = False
		while not done:
			printr(ord(next_byte))                                     # Print retrieved byte
			cp = wrap.tell()                                           # Set checkpoint
			if ord(next_byte) == sentinel[0]:                          # Check sentinel initial byte
				for i in range(5):                                 #
					i += 1                                     #
					wrap.seek(wrap.tell() + args.i)            # Skip interval
					try:    # Might reach end of file
						if ord(wrap.read(1)) != sentinel[i]:       # Check sentinel byte
							wrap.seek(cp)                      # Reset to checkpoint if not matching sentinel
							break                              #
						elif i == 5:                               #
							done = True                        # Check for sentinel
					except: # Did reach end of file
						terminate("error: Reached EOF before sentinel (No hidden file found)")
			wrap.seek(cp + args.i)                                     # Skip interval
			
			try:
				next_byte = wrap.read(1)                           # Might reach end of file
			except:
				terminate("error: Reached EOF before sentinel (No hidden file found)")
			sys.stdout.flush()
	else:
		# Using bit method
		
		done = False
		while not done:   # done set to true only when sentinel is read
			h = 0
			for i in range(8):
				w = 0
				try:
					w = ord(wrap.read(1))
				except:
					terminate("error: Reached EOF before sentinel (No hidden file found)")
				h = ((h << 1) | (w & 0b1))      # Add LSB of w to right side of h
				wrap.seek(wrap.tell() + args.i) # Skip interval
			cp = wrap.tell()                        # Set checkpoint

			if h == sentinel[0]:                    # Might be reaching sentinel
				for j in range(5):              # Repeat test for next 5 bytes
					j += 1
					k = 0
					for i in range(8):
						w = 0
						try:
							w = ord(wrap.read(1))
						except:
							terminate("error: Reached EOF before sentinel (No hidden file found)")
						k = ((k << 1) | (w & 0b1))       # Add LSB of w to right side of h
						wrap.seek(wrap.tell() + args.i)  # Skip interval
					if k != sentinel[j]:    # Looking for sentinel byte
						wrap.seek(cp)   # Reset to checkpoint
						break
					elif j == 5:
						done = True
			printr(h)                # Print retrieved byte to stdout

terminate("Finished successfully")
