age = int(input("What's your age?      "))
if age >= 0:
	print("woah that's so cool you are a: ")
	if age <= 12:
		print("Child")
	elif age <= 19:
		print("Teenager")
	elif age <= 64:
		print("Adult")
	elif age >= 65:
		print( int(age/100)*"Super " + "Senior")
else:
	print("Naughty did you put in a negative number?")
	