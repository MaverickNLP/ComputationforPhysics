import math
def f(x):
	return x**3-x-2

a = 20
b = -10
diff = abs(abs(a)-abs(b))
tol = 0.0000001

while diff > tol: 
	if f(a) * f(b) < 0:
		c = (a+b)/2
		if f(c) == 0:
			print(c)
			exit()
		elif f(c) * f(b) < 0: 
			a = c
			print(a)
		elif f(c) * f(a) < 0: 
			b = c
			print(b)
		diff = abs(abs(a)-abs(b))