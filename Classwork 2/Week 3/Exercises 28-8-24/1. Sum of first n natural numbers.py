a = input("You wish to conjure to sum of natural numbers up to:")
b = int(a)
if b < 0:
	print("Please provide a natural number!")
	exit()
else: 
	c = list(range(b+1))
	y = 0
	for i in c: 
		y += i
	print(y)