import subprocess
import re

def main():

	print("= Retrieving hidden message with Grep and Python =\n")

	currentKey = raw_input("First key: ")
	fileName = raw_input("Filename: ")

	print "\nRetrieving the message...\n"
	message = '' 

	while (True):

		command = "grep -e " + currentKey + " " + fileName

		proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
		(out, err) = proc.communicate()

		words = re.split(' ---|---|\n', out)

		if ((len(words) <= 4) and (words[0] != currentKey)):
			break

		counter = 0
		auxKey = words[counter]

		while (auxKey != currentKey):
			counter += 3
			auxKey = words[counter]
		
		letter = words[counter + 1]
		nextKey = words[counter + 2]

		if (letter == ''):
			message = message + ' '
		else:
			message = message + letter

		currentKey = nextKey

	print "Hidden message: " + message
		
main()
