###############################################################################
# Name: Samantha Santiago
# Date: 03/22/2018
# Program: vigenere.py
# Objective: Mathematically implement a Vigenere cipher to encrypt and decrypt
# messages, then display the message in the terminal. Program can write a 
# message to a .txt file, and receive input from a .txt file as well.
###############################################################################

#imports sys commands
import sys

# encryption function - works
def encrypt(text, key):
    # variables to establish a list for the encrypted message, an int for which letter we're on, range of ASCII characters to work with, and length of key
	ciphertext = ""
	on_letter = 0
	value = 0
	key_len = len(key)
	
	for i in range(0,len(text)):
		if on_letter == key_len:
			on_letter = 0
        # checks to see if the current character in text variable is a letter, then assigns ASCII value of lower/uppercase A to value
		if text[i].isalpha():
			if text[i] >= 'a' and text[i] <= 'z':
				value = 97
			elif text[i] >= 'A' and text[i] <= 'Z':
				value = 65
			# integer for the value of current plaintext character
			plain_num = ord(text[i]) - value
			# shift is the value of corresponding key character - 97, so that it becomes an ASCII value
			shift = ord(key[on_letter]) - 97
			# value of the new letter (plaintext becoming encrypted) is integer of plaintext plus the shift value
			new_letter_num = plain_num + shift
			# mod to make sure the value stays in the letter range
			if new_letter_num > 25:
				new_letter_num = new_letter_num % 26
			# value is added to integer of the new letter
			new_letter_num += value
			# integer is converted to a character
			new_letter = chr(new_letter_num)
			# the new, encrypted letter is added to the ciphertext
			ciphertext += new_letter
			# we move on to the next letter
			on_letter += 1
        # non-alpha characters are automatically added
		else:
			ciphertext += text[i]
	# ciphertext is returned - this is what gets printed in the terminal	
	return ciphertext

# decryption function - works	
def decrypt(text, key):
# variables to establish a list for the decrypted message, an int for which letter we're on, range of ASCII characters to work with, and length of key
	plaintext = ""
	on_letter = 0
	value = 0
	key_len = len(key)
	
	for i in range(0,len(text)):
		if on_letter == key_len:
			on_letter = 0
        # checks to see if the current character in text variable is a letter, then assigns ASCII value of lower/uppercase A to value
		if text[i].isalpha():
			if text[i] >= 'a' and text[i] <= 'z':
				value = 97
			elif text[i] >= 'A' and text[i] <= 'Z':
				value = 65
			# integer for the value of current ciphertext character
			ciph_num = ord(text[i]) - value
			# shift is the value of corresponding key character - 97, so that it becomes an ASCII value
			shift = ord(key[on_letter]) - 97
			# value of the new letter (ciphertext becoming decrypted) is integer of ciphertext minus the shift value, then 26 added to keep it positive
			new_letter_num = (ciph_num - shift) + 26
			# mod to make sure the value stays in the letter range
			if new_letter_num > 25:
				new_letter_num = new_letter_num % 26
			# value is added to integer of the new letter
			new_letter_num += value
			# integer is converted to a character
			new_letter = chr(new_letter_num)
			# the decrypted letter is added to the plaintext
			plaintext += new_letter
			# we move on to the next letter
			on_letter += 1
        # non-alpha characters are automatically added
		else:
			plaintext += text[i]
    # plaintext is returned - this is what gets printed in the terminal
	return plaintext

# Main function - executed once program is started	
def Main():
    # main function
	while True: 
		if (len(sys.argv) == 3):
			text = sys.stdin.readline()  # input here -  this is what gets encrypted/decrypted
			for i in range(2, len(sys.argv)):
				if text == "\n" or text == "": # catches if only enter key was hit or if there's nothing. For some reason this makes CTRL-D work, so cool.
					exit()
                # encrypt and decrypt are pretty much the same - the key is the last part on the command line, made lowercase and with spaces removed. This is then passed along with the text variable into the respective function. rstrip() gets rid of newlines following the printed message.
				if (sys.argv[1] == "-e"):
					key = ''.join(sys.argv[i].lower().replace(" ", ""))
					print encrypt(text, key).rstrip()
				elif (sys.argv[1] == "-d"):
					key = ''.join(sys.argv[i].lower().replace(" ", ""))
					print decrypt(text, key).rstrip()
                # error handling - only happens if you try anything other than -d or -e
				else:
					print "Error: unknown option. Exiting now..."
					exit()
        # error handling: catches if the command wasn't typed properly (if there wasn't enough entered, etc.)
		else:
			print "Error. Try again by typing your command as follows: python vigenere.py [-d/-e] [key]" # general error handling works
			exit()
		
Main()

###########################
# Can I just take a second to say that text == "" fixed all my remaining problems? Because it did. Adding that and making an OR statement in Main() solved all my lingering issues with this program. That's nuts.
# But I'm done, so I can't really complain, eh?
