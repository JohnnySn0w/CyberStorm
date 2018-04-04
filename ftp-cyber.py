######################################################
# Group: Greed
# Members: Alexandra Duran Chicas, Zachary Guillot, 
# Conan Howard, Oluwatoyosi Kade, Michael Mahan, 
# Darryl Rayborn, Jonathan Ruppel, Samantha Santiago
# Date: 04/04/2018
# Program: ftp-copy.py
# Objective: Takes the permissions gathered from a directory in
# an FTP, translates them into binary, and then decodes it to
# reveal a covert message.
######################################################
import ftplib, sys

def solve(login, passwd, n):
##################################################################################
	# format: python ftp-cyber.py [anonymous] [''] [directory name]
	# fetch file listing, permissions from FTP --> done
	# reference: https://stackoverflow.com/questions/111954/using-pythons-ftplib-to-get-a-directory-listing-portably
	# up until I introduce f.
	ftp = ftplib.FTP("jeangourd.com")
	ftp.login(login, passwd) # logs in
	ftp.cwd(n)

	data = []
	
	ftp.dir(data.append) # takes directory info and adds it to data above

	ftp.quit() # gets out
	# get it to export to a string instead of outputting to the command line --> done
	# checks for which directory we're in (n above for the solve argument). If not whatever is hardcoded, then the program
	# checks the first three bits of each line in the string to make sure they're not set.
	# If they're set, the line is skipped over and the next one is checked so that the seven rightmost are added to f.
	# If directory is the hardcoded one, then all 10 for each line are added.
	f = ''
	for line in data:
		if n == "new":
			f += (line[0:10])
		else:
			if line[0:3] == "---":
				f += (line[3:10])
################################################################################# 
	# Read a certain segment of the string, then have an if/else statement that turns - into 0 and drwx into 1's --> done
	g = ''
	for i in f:
		if (i == "r" or i == "w" or i == "x" or i == "d"):
			g += "1"
		elif (i == "-"):
			g += "0"
#################################################################################
	# decode file permissions with binary decoder --> done
	# I took the code from the part of my binary program where it processes 7-bits and pasted it here - Samantha Santiago
	len_seven = 7
	charac = ''.join(g.split()) # string of what's in the file
	input_str = [charac[i:i+len_seven] for i in range(0,len(charac),len_seven)]
	lista = ''.join([chr(int(c,base=2)) for c in input_str]) # holds decoded string
	print lista
#################################################################################
	# send decoded message to output --> done
#################################################################################
# main function for the program. Login, password, and directory name are the arguments needed on the command line.
def Main():
	while True:
		if (len(sys.argv) == 4):
			login = sys.argv[1]
			passwd = sys.argv[2]
			n = sys.argv[3]
			solve(login, passwd, n)
			exit()
		else:
			print "Error. Try typing your command as follows: python ftp-cyber.py [login name] [password] [directory name]"
			exit()
Main()