def main():
	x = raw_input("What's your name? ")
	a = int(raw_input("Inform an integer: "))
	b = float(raw_input("Inform a float: "))

	print("Your name is %s") % (x)
	print("Integer number: %i") % (a)
	print("Float number: %.2f") % (b)

main()