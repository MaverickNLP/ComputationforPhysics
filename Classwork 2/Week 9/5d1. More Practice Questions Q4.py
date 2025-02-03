import numpy as np
import matplotlib.pyplot as plt


def f(x):
	return x**3-6*(x**2)*11*x-6

x = np.linspace(0,4, 101, True)
fig, ax = plt.subplots()
line1 = plt.plot(x, f(x))
plt.show()
