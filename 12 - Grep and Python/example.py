import subprocess

def main():

	print("= Retrieving letter occurencies with Grep and Python =\n")

	caracter = raw_input("Character you want search for: ")
	fileName = "hiddenMessageExercise.txt"

	print "Executing the grep coomand...\n"
	
	command = "grep -e \"---" + caracter + "---\" " + fileName

	proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
	(out,err) = proc.communicate()

	if not out:
		print "No matches found"
	else:
		print "Result:\n"
		print "(Key - Character - Next key)\n"
		print out

main()