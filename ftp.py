######################################################
# Group: Greed
# Members: Alexandra Duran Chicas, Zachary Guillot, 
# Conan Howard, Oluwatoyosi Kade, Michael Mahan, 
# Darryl Rayborn, Jonathan Ruppel, Samantha Santiago
# Date: 03/28/2018
# Program: ftp.py
# Objective: 
######################################################
# this can either all be in one main function, or have one main and separate functions
import ftplib, os
# things that need to get done:
##################################################################################
# fetch file listing, permissions from FTP --> done
# reference: https://stackoverflow.com/questions/111954/using-pythons-ftplib-to-get-a-directory-listing-portably
# up until I introduce f.
ftp = ftplib.FTP("jeangourd.com")
ftp.login("anonymous", "") # logs in
# the print statements are mostly for show, but it also lets you know how quickly the process of logging in and out takes
# based on how fast it shows up
# I can take it out later, but for now, I'm leaving it.
print "\n---------------"
print "\nLogging in...\n"

data = []

ftp.dir(data.append) # takes directory info and adds it to data list above

ftp.quit() # gets out of the FTP
print "Logging out...\n"
print "---------------\n"

f = open("directory.txt", "w+") # the plus at the end of w means that if the file doesn't exist, it will be created
for line in data:
	f.write(line + "\n")
f.close() # always remember close() after using open. Needs to be done whenever modes are switched or you're done
		  # with a file.
# get it to export to a .txt file instead of outputting to the command line --> done
#################################################################################
# use a function so that when it reads string lines in the .txt file, it only counts [1:11] 
# onward (so like [1:11] or something), with the first three bits of each getting ignored 
# along with the rest of the string. then have an if/else statement that turns - into 0 and rwx into 1's --> done
f = open("directory.txt", "r")
g = open("holder.txt", "w+") #identical file for now, but it will hold the parts of directory.txt that we actually need
if f.mode == "r":
	for line in f:
		g.write(line[1:10] + "\n") # changed up here so that the program ignores the space at the end of each line
g.close()
f.close()

g = open("holder.txt", "r")
h = open("numbers.txt", "w+")

if g.mode == "r":
	for line in g:
		l = list(line)
		print l # this is just to check to see what got captured by holder.txt
		for i in l:
			if (i == "r" or i == "w" or i == "x"):
				h.write("1")
			elif (i == "-"):
				h.write("0")
			else:
				pass
g.close()
h.close()
#################################################################################
# decode file permissions with binary decoder
# still needs work - not returning correctly. However, it does count 90 total characters and ignores \n, so
# it's getting somewhere
h = open("numbers.txt", "r")
if h.mode == "r":
	n = h.read()
	print n
	print(len(n)) # more checking. 90 total 0's and 1's
h.close()
#################################################################################
# send decoded message to output
# still needs to be done
#################################################################################
# gets rid of files we created for this program. Only included for the sake of convenience (Gourd's especially)
# reference: https://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist
# for the try-except loop idea,which also handles OSError
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
