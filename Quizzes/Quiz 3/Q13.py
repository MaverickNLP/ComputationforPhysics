import math
def f(x):
	return math.exp(x)-2
def f_dash(x):
	return math.exp(x)
x0 = 200
diff = 1
tol = 0.001
while diff > tol:
	print(x0)
	x1 = x0 - f(x0)/f_dash(x0) # Woops wrong sign.
	diff = abs(x1-x0)
	x0 = x1

print(x0)