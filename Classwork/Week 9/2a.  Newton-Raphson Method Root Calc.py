import math
def f(x):
	return x**2-2 
def g(x):
	return 2*x

x0 = 10
diff = abs(f(x0))
tol = 0.0001
while diff > tol:
	print(x0)
	x1 = x0 - f(x0)/g(x0)
	diff = abs(f(x1))
	x0 = x1
print(x0)