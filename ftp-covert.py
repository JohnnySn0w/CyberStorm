######################################################
# Group: Greed
# Members: Alexandra Duran Chicas, Zachary Guillot, 
# Conan Howard, Oluwatoyosi Kade, Michael Mahan, 
# Darryl Rayborn, Jonathan Ruppel, Samantha Santiago
# Date: 03/28/2018
# Program: ftp-covert-channel.py
# Objective: 
######################################################
# this can either all be in one main function, or have one main and separate functions

# things that need to get done:
##################################################################################
# fetch file listing, permissions from FTP --> done
# reference: https://stackoverflow.com/questions/111954/using-pythons-ftplib-to-get-a-directory-listing-portably
# up until I introduce f (excluding print statements. Those are mine to test stuff flows).
import ftplib

ftp = ftplib.FTP("jeangourd.com")
ftp.login("anonymous", "") # logs in
print "\nLogging in...\n"

data = []

ftp.dir(data.append) # takes directory info and adds it to data list above

ftp.quit() # gets out of the FTP
print "Logging out...\n"

f = open("directory.txt", "w+") # the plus at the end of w means that if the file doesn't exist, it will be created
for line in data:
	f.write(line + "\n")
f.close() # always remember f.close()!
# get it to export to a .txt file instead of outputting to the command line --> done
#################################################################################
f = open("directory.txt", "r")
if f.mode == "r":
	for line in data:
		print(f.readline()) # this just tests to make sure reading the txt file works
f.close()
# use a function so that when it reads string lines in the .txt file, it only counts [3:] 
# onward (so like [3:11] or something), with the first three bits of each getting ignored 
# along with the rest of the string. then have an if/else statement that turns - into 0 and rwx into 1's
#################################################################################
# decode file permissions with binary decoder
#################################################################################
# send decoded message to output
#################################################################################
