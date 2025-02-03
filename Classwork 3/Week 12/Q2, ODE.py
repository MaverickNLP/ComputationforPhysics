import numpy as np
import matplotlib.pyplot as plt
time_array_1 = np.linspace(0,5, 51, True)
time_array_2 = np.linspace(0,5, 51, True)

y_array_1 = [0.1]
y_array_2 = [1.1]
for i in time_array_1:
	ycurrent_1 = y_array_1[-1]
	delta_y_1 = ycurrent_1*(1-ycurrent_1)
	ynew_1 = ycurrent_1 + delta_y_1
	y_array_1.append(ynew_1)

for i in time_array_2:
	ycurrent_2 = y_array_2[-1]
	delta_y_2 = ycurrent_2*(1-ycurrent_2)
	ynew_2 = ycurrent_2 + delta_y_2
	y_array_2.append(ynew_2)

y_array_1 = y_array_1[0:-1]
y_array_2 = y_array_2[0:-1]

line_1 = plt.plot(time_array_1,y_array_1)
line_2 = plt.plot(time_array_2,y_array_2)

plt.show()

print(y_array_1[-1])
print(y_array_2[-1])