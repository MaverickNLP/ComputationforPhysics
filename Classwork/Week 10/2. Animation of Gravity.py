import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

fig, ax = plt.subplots()
t = np.linspace(0, 10, 100)
g = -9.81
y_value = g*(t**2)/2
x_value = [9]*t
line1 = ax.plot(x_value[0], y_value[0])[0]

def update(frame):
	x = x_value[:frame]
	y = y_value[:frame]
	line1.set_xdata(x)
	line1.set_ydata(y)
	return (line1)
ani = anim.FuncAnimation(fig=fig, func = update, frames = 100, interval = 3)
plt.ylim(y_value[-1], 0)
plt.xlim(0,2)
plt.show()