def factorial(n):
	product = 1
	while n > 1:
		product = product * n
		n -= 1
	return product
print(factorial(1000))