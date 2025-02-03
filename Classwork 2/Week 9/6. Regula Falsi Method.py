import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x**2-4

a = 1
b = 10
diff = abs(abs(a)-abs(b))
tol = 0.0001
while diff > tol:
	c = b - (f(b)*(b-a))/(f(b)-f(a))
	if f(c)*f(b)<0:
		a = c
		diff = abs(a)-abs(b)
	elif f(c)*f(a)<0:
		b = c
		diff = abs(a)-abs(b)
		print(c)	

		