import numpy as np
import matplotlib.pyplot as plt

k=2
b=0.1
def acceleration(x,x_dot):
	return -k*x-b*x_dot
time_array = [0]
x_array = [1]
x_dot_array = [0]
a_array = [0]
time_delta = 0.001
time_limit = 100
count = 0
while time_array[-1] <= time_limit:
	new_time = time_array[-1]+time_delta
	time_array.append(new_time)
	x_old = x_array[-1]
	x_dot_old = x_dot_array[-1]
	a_new = acceleration(x_old, x_dot_old)
	x_dot_new = x_dot_old + a_new*time_delta
	x_new = x_old + x_dot_old*time_delta
	x_array.append(x_new)
	x_dot_array.append(x_dot_new)
	a_array.append(a_new)



plt.plot(time_array,x_array)
print(count)
plt.show()

