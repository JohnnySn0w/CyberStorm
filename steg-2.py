import sys, binascii, itertools

# declared a bunch of variables and some arrays up here; offset and interval change later
offset = 0
interval = 0
wrapper_file = ""
hidden_file = ""
byte_store = []
more_store = []
# for when the hidden file is involved in storage
byte_hidden = []
store_hidden = []
# for new file in retrieve
file_array = [] 
# counters
i = 0
j = 0

sentinel = [chr(0x0), chr(0xFF), chr(0x0), chr(0x0), chr(0xFF), chr(0x0)]	
# length of binary of the sentinel, since each character is 8 bits, so 8*6=48
sent_num = 48
sent_bin = "000000001111111100000000000000001111111100000000"
############################################################
# storage function
def storage(file, offset, interval):
	hide = sys.argv[1:]
	for h in hide:
		if "-h" in h:
			hidden_file = r[2:]
			with open(hidden_file, "rb") as g:
				bye = g.read(1)
				while bye != "":
					store_hidden.append(bye)
					bye = g.read(1)
			g.close()
			# convert to binary values from what we got from the file above - Stack Overflow
			for s in store_hidden:
				store_hidden.append(''.join('{0:08b}'.format(x, 'b') for x in bytearray(s)))
				
			# detect if byte or bit shall be executed
			bits = sys.argv[1:]
			# open file, read, append to an array
			with open(file, "rb") as f:
				by = f.read(1)
				while by != "":
					byte_store.append(by)
					by = f.read(1)
			f.close()
			# reference: https://stackoverflow.com/questions/4344017/how-can-i-get-the-concatenation-of-two-lists-in-python-without-modifying-either
			c = itertools.chain(byte_store, sentinel)
			# convert to binary values from what we got from the file above - Stack Overflow
			for b in c:
				more_store.append(''.join('{0:08b}'.format(x, 'b') for x in bytearray(b)))
			if "-B" in bits:
				more_store[offset] = store_hidden[i]
				offset += interval
			else:
				for k in range(8):
					more_store[offset] = str(bin(int(more_store[offset],2) & int("11111110", 2))[2:].zfill(8))
					more_store[offset] = str(bin(int(more_store[offset],2) | ((int(store_hidden[j],2) & int("10000000")) >> 7))[2:].zfill(8))
					store_hidden[j] = str(bin(int(store_hidden[j],2) << 1)[2:].zfill(8))
					offset += 1
				j += 1
		else:
			print "Error: nothing to hide!"
			quit()

############################################################
#retrieve function
def retrieval(file, offset, interval):
	# detect if byte or bit shall be executed
	bits = sys.argv[1:]
	# open file, read, append to an array
	with open(file, "rb") as f:
		by = f.read(1)
		while by != "":
			byte_store.append(by)
			by = f.read(1)
	f.close()
	# convert to binary values from what we got from the file above - Stack Overflow
	for b in byte_store:
		more_store.append(''.join('{0:08b}'.format(x, 'b') for x in bytearray(b)))
	if "-B" in bits:
		while sent_bin not in ''.join(file_array[-sent_num:]):
			file_array.append(more_store[offset])
			offset += interval

		# stdout with the sentinel removed. took some trial and error because
		# I forget how to count sometimes in programming.
		# referenced stack overflow because I forgot how to do stdout in python for a minute	
		for a in file_array[:-7]:
			sys.stdout.write(chr(int(a,2))) 
			
	else:
		while sent_bin not in ''.join(file_array[-sent_num:]):
			blanks = ""
			for b in range(8):
				blanks += more_store[offset][7]
				offset += 1
			file_array.append(blanks)
		for a in file_array[:-7]:
			sys.stdout.write(chr(int(a,2))) 
	for a in more_store:
		sys.stdout.write(chr(int(a,2)))
###################################
# main function
def main():
	# get values for variables above
	# referenced codingbat for the string stuff. That website really drove substrings home.
	running = sys.argv[1:]
	for r in running:
		if "-o" in r:
			offset = int(r[2:])
		if "-i" in r:
			interval = int(r[2:])
		if "-w" in r:
			wrapper = r[2:]
	
	# see which function we're about to go to
	mode = sys.argv[1:]
	for i in mode:
		if "-s" in i:
			wrapper_file = storage(wrapper, offset, interval)
		if "-r" in i:
			wrapper_file = retrieval(wrapper, offset, interval)
########################
main()
