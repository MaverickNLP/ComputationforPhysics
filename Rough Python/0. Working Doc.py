import numpy as np
import matplotlib.pyplot as plt  
from matplotlib.widgets import Slider
import math as mt

# Parametrized Function to be plotted:
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
line1, = ax.plot(x, taylor_sin(x, Terms_of_Taylor))
ax.set_xlabel("x",fontdict=Axis_title_font)
ax.set_ylabel("Sin(x)", fontdict=Axis_title_font)

axn = fig.add_axes([0.25,0,0.65,0.03])
n_slider = Slider(axn, "Terms of Taylor Series Expansion of sin(x)", 0, 20, valinit=Terms_of_Taylor, valfmt='%d', valstep=1) # I needed to make valsteps = 1. Not sure how to skip parameters in Python, and at this point I'm afraid to ask.

def update(val):
	line1.set_ydata(taylor_sin(x, n_slider.val))
	fig.canvas.draw_idle()
	

n_slider.on_changed(update)

plt.show()