import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x**2-4*x+3
def f_dash(x, h):
	return (f(x+h) - f(x))/h

x0 = -10

tol = 0.000001

diff = 1

while diff > tol:
	x1 = x0 - f(x0)/f_dash(x0, 0.0001)
	diff = abs(f(x0)-f(x1))
	x0 = x1
	print(x1)
