S = int(input("give me a number any number"))
x = int(input("guess the square root of the number you gave me"))
tol = 0.0000001
diff = 1
while diff > tol:
	newx = (x+S/x)/2
	diff = abs(x-newx)
	x = newx
	print(x)