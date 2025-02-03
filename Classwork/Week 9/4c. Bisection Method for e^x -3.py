import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return math.e**x-3

a = 2
b = 0
tol = 0.0001

while a-b > tol:
	if f(a)*f(b)<0:
		c = (a+b)/2
		if f(c)*f(b)<0:
			a = c
		elif f(c)*f(a)<0:
			b = c

print(c)