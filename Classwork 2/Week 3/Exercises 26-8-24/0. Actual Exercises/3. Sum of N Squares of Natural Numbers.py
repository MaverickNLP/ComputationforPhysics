input = input("You wish to conjure the sum of the squares of the natural numbers up to:")
input = int(input)
a = range(input+1)
b = 0
for i in a: 
	b+= i**2
print(b)