import math
def f(x):
	return (x+3/x)/2

def g(x):
	return abs(x-f(x))

tol = 0.00000001
diff = 10
pie = math.pi
x0 = 1
while diff > tol:
	print(x0)
	x1 = f(x0)
	diff = abs(g(x1))
	x0 = x1
print(x0)