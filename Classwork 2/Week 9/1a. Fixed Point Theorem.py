import math
def f(x):
	return math.cos(x)

def g(x):
	return abs(x-math.cos(x))

tol = 0.00000001
diff = 10
pie = math.pi
x0 = 10%pie
while diff > tol:
	x1 = f(x0)
	diff = abs(g(x1))
	x0 = x1
	print(x0)