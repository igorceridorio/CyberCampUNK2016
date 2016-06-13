def main():

	print "Multiplication tables!\n"

	for x in range(2, 5):
		for y in range(1, 11):
			print "%d x %d = %d" % (x, y, y * x)
		print"\n"

main()