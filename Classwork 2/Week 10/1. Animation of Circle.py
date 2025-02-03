import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim



fig, ax = plt.subplots()
t = np.linspace(0, 2*np.pi, 40)
R = 1
x_value = -R*np.cos(t)
y_value = R*np.sin(t)
line1 = ax.plot(x_value[0], y_value[0])[0]

def update(frame):
	x = x_value[:frame]
	y = y_value[:frame]
	line1.set_xdata(x_value[:frame])
	line1.set_ydata(y_value[:frame])
	return (line1)
ani = anim.FuncAnimation(fig=fig, func = update, frames = 40, interval = 30)
plt.ylim(-1, 1)
plt.xlim(-1,1)
plt.show()