def main():
	name = raw_input("Inform your full name: ")
	age = int(raw_input("Inform you age: "))
	sub1name = raw_input("First subject: ")
	sub1grade = float(raw_input("First subject grade: "))
	sub2name = raw_input("Second subject: ")
	sub2grade = float(raw_input("Second subject grade: "))
	sub3name = raw_input("Third subject: ")
	sub3grade = float(raw_input("Third subject grade: "))

	print "\nReport Card"
	print "\nStudent: %s Age: %i" % (name, age)
	print "\tSubject: %s. Grade: %.2f" % (sub1name, sub1grade)
	print "\tSubject: %s. Grade: %.2f" % (sub2name, sub2grade)
	print "\tSubject: %s. Grade: %.2f" % (sub3name, sub3grade)

main()