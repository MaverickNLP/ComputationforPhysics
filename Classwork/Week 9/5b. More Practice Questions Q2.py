import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x**2-4*x+3

a = 2.1
b = 5.1

tol = 0.0001
diff = abs(abs(b) - abs(a))

print(f(a), f(b))

while diff > tol:
	if f(a)*f(b)<0:
		c = (a+b)/2
		if f(a)*f(c)<0:
			b = c
			print(b)
		elif f(b)*f(c)<0:
			a = c
			print(a)
	diff = abs(abs(a)-abs(b))
else:
		exit()
print(c)
