def fibonacci(n):
	if n == 0:
		return 1 # Question calls for f(0) = 0, however that wouldn't work since we need ratios, and F(0), would yield F(1)/F(0) = Undefined (since we can't divide by 0)
	elif n == 1: 
		return 1 # Defines 1, 1, for the fib seq
	else:
		return fibonacci(n-1) + fibonacci(n-2) # Returns the other terms for the fib sequence

fib_seq = []
max = float(input("You want the fibonacci numbers upto?   "))
i = 0
while fibonacci(i) < max:
	fib_seq.append(fibonacci(i))
	i += 1
print(fib_seq)