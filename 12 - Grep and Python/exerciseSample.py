import subprocess

def main():

	print("= Retrieving hidden message with Grep and Python =\n")

	print "\nRetrieving the message...\n"

	message = ""
	fileName = "hiddenMessageSample.txt"

	#-------------------------------------

	command = "grep -e \"OTY33NVL1BRCC000SBZNP817TOR5I6 \" " + fileName

	proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()

	words = out.split("---");

	message += words[1]

	#-------------------------------------

	command = "grep -e \"B05P9LHVGDX994LV168YOHDRQW11GU \" " + fileName

	proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()

	words = out.split("---");

	message += words[1]

	#------------------------------------

	command = "grep -e \"G97TVIBZUE7WE1D4GQRAAS0NWYAZRE \" " + fileName

	proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()

	words = out.split("---");

	message += words[1]

	#------------------------------------

	command = "grep -e \"NVD34FU5L59OML7VW95PJG1158V2A5 \" " + fileName

	proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()

	words = out.split("---");

	message += words[1]	

	#------------------------------------	

	print "Final message: " + message
		
main()
