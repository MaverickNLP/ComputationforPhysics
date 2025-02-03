import math
def f(x):
	return math.tan(x) - x
def g(x, h):
	return (f(x+h)-f(x))/h

x0 = -4.5 
tol = 0.0001
diff = 1
while diff > tol:
	print(x0)
	x1 = x0 - f(x0)/g(x0, 0.00001)
	diff = abs(f(x1))
	x0 = x1
print(x0)