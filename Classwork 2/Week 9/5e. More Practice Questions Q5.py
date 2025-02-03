import numpy as np
import matplotlib.pyplot as plt

y_array = [0.7]
x0 = 0.7
r = 1.5 

tol = 0.001
diff = 1
length = 1
while diff > tol:
	if y_array[-1] < 0.5:
		y_array.append(r*y_array[-1])
		diff = abs(y_array[-1]-y_array[-2])
		length += 1
	elif y_array[-1] >= 0.5:
		y_array.append(r*(1-y_array[-1]))
		diff = abs(y_array[-1]-y_array[-2])
		length += 1
x_array = list(range(1, length+1))

print(y_array, length, x_array)
line1 = plt.plot(x_array, y_array)
plt.show()
