def f(x):
	return x**2-5
def g(x, h):
	return (f(x+h)-f(x))/h

x0 = 1.4 # r = 1, 2, 3 all roots so need to have many trials of different x0s.
tol = 0.0001
diff = 1
while diff > tol:
	print(x0)
	x1 = x0 - f(x0)/g(x0, 0.00001)
	diff = abs(f(x1))
	x0 = x1
print(x0)