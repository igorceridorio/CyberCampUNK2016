def main():

	print "WHILE loop\n"
	y = 0
	while y < 5:
		print "y value is: %d" % (y)
		y = y + 1;

	print "\nFOR loop\n"
	for x in range(0, 5):
		print "x value is: %d" % (x)

	print "\nFOR loop with string\n"
	sentence = "Python is easy!"
	for letter in sentence:
		print "%c" % (letter)

main()