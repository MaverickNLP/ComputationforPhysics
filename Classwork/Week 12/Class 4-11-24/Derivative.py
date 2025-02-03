import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
dx = x[1]-x[0]
y = np.sin(x)
dydx_fe = (np.roll(y, -1)-y)/dx
dydx_fe = dydx_fe[:-1]
plt.plot(x,y)
x = x[:-1]
plt.plot(x, dydx_fe)

plt.show()