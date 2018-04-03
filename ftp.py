######################################################
# Group: Greed
# Members: Alexandra Duran Chicas, Zachary Guillot, 
# Conan Howard, Oluwatoyosi Kade, Michael Mahan, 
# Darryl Rayborn, Jonathan Ruppel, Samantha Santiago
# Date: 04/02/2018
# Program: ftp.py
# Objective: 
######################################################
import ftplib, os

def solve(n):
##################################################################################
	# fetch file listing, permissions from FTP --> done
	# reference: https://stackoverflow.com/questions/111954/using-pythons-ftplib-to-get-a-directory-listing-portably
	# up until I introduce f.
	ftp = ftplib.FTP("jeangourd.com")
	ftp.login("anonymous", "") # logs in
	ftp.cwd(n)

	data = []

	ftp.dir(data.append) # takes directory info and adds it to data list above

	ftp.quit() # gets out of the FTP
	# get it to export to a .txt file instead of outputting to the command line --> done
	f = open("directory.txt", "w+") # the plus at the end of w means that if the file doesn't exist, it will be created
	for line in data:
		f.write(line + "\n")
	f.close() # always remember close() after using open. Needs to be done whenever modes are switched or you're done with a file.
################################################################################# 
	# Read a certain segment of the string, then have an if/else statement that turns - into 0 and drwx into 1's --> done
	f = open("directory.txt", "r")
	g = open("holder.txt", "w+") # holds just the permissions -- here mostly for debugging purposes
	if f.mode == "r":
		for line in f:
			if n == "10": # hardcoded to be specific for directory 10. Otherwise, it will default to ignoring permissions with the first three 'set' and taking the seven rightmost bits
				g.write(line[0:10] + "\n") # changed up here so that the program ignores the space at the end of each line.
			else:
				if ('d' in line [0:3] or 'r' in line[0:3] or 'w' in line[0:3] or 'x' in line[0:3]): # works so that it only uses the if statement if the character is contained within this
					line.strip()
				else:
					g.write(line[3:10] + "\n") 
	g.close()
	f.close()

	g = open("holder.txt", "r")
	h = open("numbers.txt", "w+") # here to hold our binary

	if g.mode == "r":
		for line in g:
			l = list(line)
			#print l # this is just to check to see what got captured by holder.txt
			for i in l:
				if (i == "r" or i == "w" or i == "x" or i == "d"):
					h.write("1")
				elif (i == "-"):
					h.write("0")
				else:
					pass
	g.close()
	h.close()
#################################################################################
	# decode file permissions with binary decoder --> done
	h = open("numbers.txt", "r")
	m = open("textfile.txt", "w+")
	# I took the code from the part of my binary program where it processes 7-bits and pasted it here - Samantha Santiago
	if h.mode == "r":
		characters = 0
		len_seven = 7
		n = h.read()
		#print n
		#print(len(n)) # more checking.
		charac = ''.join(n.split()) # string of what's in the file
		characters += sum(len(chara) for chara in charac) # integer needed for mod check
		input_str = [charac[i:i+len_seven] for i in range(0,len(charac),len_seven)]
		lista = ''.join([chr(int(c,base=2)) for c in input_str]) # holds decoded string
		m.write(lista) # writes to file for debugging purposes
		print lista # prints lista
	h.close()
#################################################################################
	# send decoded message to output --> done
#################################################################################
	# gets rid of files we created for this program. Only included for the sake of convenience (Gourd's especially)
	# reference: https://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist
	# for the try-except loop idea, which also handles OSError
	# I have multiple files set up so that every step so far can be checked. Just comment out what's necessary.
	# I will go back and make it all to just one file once it all works.
	try:
		os.remove("directory.txt")
	except OSError:
		pass
	
	try:
		os.remove("holder.txt")
	except OSError:
		pass
	
	try:
		os.remove("numbers.txt")
	except OSError:
		pass
	try:
		os.remove("textfile.txt")
	except OSError:
		pass
#################################################################################
# calls function to solve for the home directory, 7, and 10
solve('~')
solve("7")
solve("10")
#################################################################################
