import numpy as np
import matplotlib.pyplot as plt 
def x_dot(x): #oops used english instead of code
	return np.cos(x)-x 

time_array = [0] 
x_array = [0] 
delta_x = 1 
time_delta = 0.1 
while delta_x > 10**-6: # I messed up the direction of the greater than or less than sign here. 
	x_old = x_array[-1]
	x_new = x_old + x_dot(x_old)*time_delta 
	x_array.append(x_new) 
	time_array.append(time_array[-1]+time_delta)
	delta_x = abs(x_new-x_old)
plt.plot(time_array, x_array)
print(time_array)
print(x_array)
plt.show()
