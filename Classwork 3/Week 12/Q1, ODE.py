import numpy as np
import matplotlib.pyplot as plt

time_array_2 = np.linspace(0,5, 501, True)

k = -0.5
y_array_1 = [1]
y_array_2 = [1]

def nat(x):
	return np.e**(k*x)


for i in time_array_2:
	ycurrent_2 = y_array_2[-1]
	delta_y_2 = (k)*(ycurrent_2)
	ynew_2 = ycurrent_2 + delta_y_2
	y_array_2.append(ynew_2)

y_array_1 = y_array_1[0:-1]
y_array_2 = y_array_2[0:-1]
e_array_2 = []
for i in time_array_2:
	e_array_2.append(nat(i))

line_1 = plt.plot(time_array_2, e_array_2)
line_2 = plt.plot(time_array_2,y_array_2)

plt.show()

print(y_array_1[-1])
print(y_array_2[-1])