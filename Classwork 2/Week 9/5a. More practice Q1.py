import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x**2-4*x+3

a = np.linspace(-2, 6,81, True)
b = list(range(81))
for i in b: 
	b[i] = f(a[i])
fig, ax = plt.subplots( )
line1 = ax.plot(a, f(a))
line2 = ax.plot(a-1, b)
plt.show()