import numpy as np 
import matplotlib.pyplot as plt
def f(x):
	return 3*(x**2) - 5*x-1 # I like to put brackets for x**2 for clarity
a = 1
b = 2
tol = 0.0001
diff = 1 # just has to be > tol for the first check
while diff > tol:
	if f(a)*f(b) < 0: # I like adding this line so that I don't have to actually do anything.
		c= (a+b)/2
		if f(c)*f(b)<0:
			a = c
			diff = abs(b-a)
			print(c)
		elif f(c) *f(a)<0:
			b = c
			diff = abs(b-a)
			print(c)
	else:
		print("Use different numbers!")