import numpy as np
import matplotlib.pyplot as plt  
from matplotlib.widgets import Slider
import math as mt

# Function to be plotted:
sum = 0
def taylor_sin(x, n):
	x = x%(2*(mt.pi))
	sin_x_1 = ((-1)**n)
	sin_x_2 = x**(2*n+1)
	sin_x_3 = mt.factorial(2*n+1)
	sin_x = (sin_x_1)*(sin_x_2)/(sin_x_3) # For some reason just assigning sin x = "" was creating a 'float' not callable error. I decided to use less brackets and fix the error, this ensures that python doesn't accidentally misinterpret some operators as functions.
	global sum
	sum += sin_x
	if n > 0:
		return(taylor_sin(x,n-1))
	if n == 0:
		return sum
	if n < 0:
		print("Give me a natural number please :)")

# Aesthetics
title_font = {'family': 'AppleGothic',
		'color': 'black',
		'size': '14',
		}
Axis_title_font = {'family': 'AppleGothic',
		'color': 'black',
		'size': '12',
		}
Legend_text = {'family': 'Times New Roman',
			   'color': 'black',
			   'size':'10'}

# Graphing, defining values, etc. 
range_of_singraph = float(input("You wish to compare value of sine using the Taylor Approximation and sin(x) function in python from 0 radians upto?    "))
density_of_singraph = int(input("How many values of sine would you like to use to make this comparision?   "))
Terms_of_Taylor = int(input("How many terms of the Taylor Series would you like to use for this calculation right now, (Please give a value between 1 and 20)?   "))

if Terms_of_Taylor in list(range(1, 21)):
	print("Good job") 
else:
	print("Please provide a value between 1 and 20") 
	exit()

fig, ax = plt.subplots()
x = np.linspace(0, range_of_singraph, density_of_singraph)
sin_x = list(range(density_of_singraph))
zero_line = np.zeros([density_of_singraph])
for i in sin_x:
	sin_x[i] = mt.sin(x[i])
line2 = ax.plot(x, abs(taylor_sin(x, Terms_of_Taylor) - sin_x), linestyle='dashed')
line1 = ax.plot(x, zero_line)
ax.set_xlabel("x",fontdict=Axis_title_font)
ax.set_ylabel("|Δsin(x)| of approximations", fontdict=Axis_title_font)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_title("Error in approximations of sin(x)", fontdict=title_font)

# Question 4:
# As n increases the approximaiton of sin(x) becomes applicable to a wider range of values. At 10 values however, the difference between the
# approximation and 'real' values suggested by the math module becomes almost zero, with a magnitude of 10e-14. If you graph upto some crazy 
# number like 10000, a roughly linear pattern emerges, with a best fit line of approximately y = 4*10e-17*|x|. Which also implies an error of 0.
# This error is interesting, since I'm not sure what kind of algorithm Python's math module uses to calculate sine. But this problem seems to 
# suggest that it does not use a taylor series. Perhaps there's a more computationally efficient method of solving for the sin of some number.
# 
# Question 5:
# As n increases our approximation error also increases. But this is also limited since we're for any absolute values of theta that are greater than 
# 2pi we reference to values between 0 and pi using line 9 of the code. On second thought the implication here is that Python's math module's
# values are getting further away from the values that taylor_sin(x, n) returns. 

# There are also some spikes here and there which are perhaps somewhat interesting. 

plt.show()