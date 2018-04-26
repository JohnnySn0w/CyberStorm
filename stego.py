######################################################
# Group: Greed
# Members: Alexandra Duran Chicas, Zachary Guillot, 
# Conan Howard, Oluwatoyosi Kade, Michael Mahan, 
# Darryl Rayborn, Jonathan Ruppel, Samantha Santiago
# Date: 04/26/2018
# Program: stego.py
# Objective: Program stores and retrieves hidden things
# from within other things, called 'wrappers'.
######################################################

import sys, binascii

# declared a bunch of variables and some arrays up here; offset and interval are set as "defaults" here
offset = 1024
interval = 8
hide_store = []
more_store = []
file_array = [] 
# counters
i = 0
j = 0

sentinel = [chr(0x0), chr(0xFF), chr(0x0), chr(0x0), chr(0xFF), chr(0x0)]	
# length of binary of the sentinel, since each character is 8 bits, so 8*6=48
sent_num = 48
sent_bin = "000000001111111100000000000000001111111100000000"

############################################################
# file opening function -- initialize array, open file, read/store binary to array, clear array, close file
def open_up(file):
	wrapper_store = []
	with open(file, "rb") as f:
		by = f.read(1)
		while by != "":
			wrapper_store.append(by)
			by = f.read(1)
	return wrapper_store
	wrapper_store = [] # clears out array in case function has to be used again immediately (such as with storage)
	f.close()
############################################################
# storage function
def storage(hidden, file, offset, interval):
	bits = sys.argv[1:]
	j = 0
	# open hidden file and store to array; add sentinel to the end of the array; convert to binary; and store on bytearray 	
	hide = open_up(hidden)
	hide.extend(sentinel)
	for b in hide:
		hide_store.append(''.join('{0:08b}'.format(x, 'b') for x in bytearray(b)))
	
	# open wrapper file and store to array; add sentinel to the array; convert to binary; and store on bytearray 
	wrap = open_up(file)
	for b in wrap:
		more_store.append(''.join('{0:08b}'.format(x, 'b') for x in bytearray(b)))
	
	# executes the meat of this function as long as i != the length of our hidden file bytearray
	for i in range(len(hide_store)):
		# byte mode - wrapper bytearray item is made equal to hidden bytearray item; offset is then incremented by the interval
		if "-B" in bits:
			more_store[offset] = hide_store[i]
			offset += interval
		# bit mode - for each item in wrapper bytearray, we go on a smaller scale to the bits within each byte
		else:
			for k in range(0,8):
				# most of this was referenced from Stack Overflow
				# item in wrapper bytearray (at offset) is converted to an actual binary number for bitwise ops, and then AND with 11111110. Item is then converted back to string and where the first two (0b) are left off
				more_store[offset] = str(bin(int(more_store[offset],2) & int("11111110",2))[2:].zfill(8))
				# item in wrapper bytearray is converted to actual binary for bitwise ops again, and then OR with the result of AND hidden bytearray number and 100000000, shifted right by 7.
				# item is then converted back to string where the first two (0b) are left off
				more_store[offset] = str(bin(int(more_store[offset],2) | ((int(hide_store[j],2) & int("10000000")) >> 7))[2:].zfill(8))
				# hidden bytearray at j is shifted left by 1, converted back to string where first two characters are left off.
				hide_store[j] = str(bin(int(hide_store[j],2) << 1)[2:].zfill(8))
				offset += 1
			j += 1
	# write out to stdout
	for m in more_store:
		sys.stdout.write(chr(int(m,2)))	
	
############################################################
#retrieve function
def retrieval(wrapper, offset, interval):
	bits = sys.argv[1:]
	# open up file, store in array
	wrap = open_up(wrapper)
	# convert to binary values from what we got from the file above - Stack Overflow
	for b in wrap:
		more_store.append(''.join('{0:08b}'.format(x, 'b') for x in bytearray(b)))
	# byte mode
	if "-B" in bits:
		# as long as the sentinel binary isn't found, add to file array and increment offset by interval
		while sent_bin not in ''.join(file_array[-sent_num:]):
			file_array.append(more_store[offset])
			offset += interval

	# bit mode
	else: 
		# as long as the sentinel binary isn't found, add to file array and increment offset by interval
		while sent_bin not in ''.join(file_array[-sent_num:]):
			blanks = "" # string of data for file
			# get on bit scale
			for b in range(0,8):
				blanks += more_store[offset][7] # blanks is appended here
				offset += 1 # offset adjusted by 1
			file_array.append(blanks) # array representing file is appended with bytes
		
	# file array is written to stdout, except the last six bytes (that's the sentinel)
	# ref: stackoverflow
	for a in file_array[:-7]:
		sys.stdout.write(chr(int(a,2)))
###################################
# main function
def main():
	# get values for variables above
	# referenced codingbat for the string stuff. That website really loves substrings.
	running = sys.argv[1:]
	for r in running:
		if "-o" in r:
			offset = int(r[2:])
		if "-i" in r:
			interval = int(r[2:])
		if "-w" in r:
			wrapper = r[2:]
		if "-h" in r:
			hidden = r[2:]
	
	# see which function we're about to go to
	mode = sys.argv[1:]
	for i in mode:
		if "-s" in i:
			storage(hidden, wrapper, offset, interval)
		if "-r" in i:
			retrieval(wrapper, offset, interval)
########################
main()
# runs program :D
