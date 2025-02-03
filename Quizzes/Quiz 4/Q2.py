import numpy as np
import matplotlib.pyplot as plt

m = 0.1 
g = -10
b = 1 
tol = 10**-8 #tol was setup wrong because i just copied the value from the question oooooops 
delta_time = 0.01

time_array=[0]
y_array=[0]
v_array=[0]
a_array=[]
delta_v = 1

def y_dotdot(x): #used english instead of code
	return g-(b/m)*x

while delta_v > tol:
	y_old = y_array[-1]
	v_old = v_array[-1]
	a_new = y_dotdot(v_old)
	v_new = v_old + a_new*delta_time
	y_new = y_old + v_new*delta_time
	a_array.append(a_new)
	v_array.append(v_new)
	y_array.append(y_new)
	time_array.append(time_array[-1]+delta_time)
	delta_v = abs(v_new - v_old) #Forgot absolute sign 

plt.plot(time_array, y_array)
print(tol)
plt.plot(time_array, v_array) 


plt.show()
# i wrote extensively about this for high school very fun to revisit the topic yay 