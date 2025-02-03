year = int(input("gimme a number any number pls pls pls:       "))

A = bool(year%4)
B = bool(year%100)
C = bool(year%400)

if ((A or C) and B):
	print("that is a leap year")
else:
	print('not leap year')




#A = bool(year%4)
#B = bool(year%100)
#C = bool(year%400)
#print(A,B,C)
#if A + B + C == 0:
#	print("That's a leap year!")
#elif A + B + C == 2: 
#	print("That's a leap year!")
#elif A + B + C == 1:
#	print("That's not a leap year!")
#elif A + B + C == 3: 
#	print("That's not a leap year!")



#if year%4 == 0: 
#	if year%100==0:
#		if year%400 == 0:
#			print("That's a leap year!!")
#		else:
#			print("That isn't a leap year :(")
#	else:
#		print("That's a leap year!!")
#else:
#	print("That isn't a leap year :(")
	