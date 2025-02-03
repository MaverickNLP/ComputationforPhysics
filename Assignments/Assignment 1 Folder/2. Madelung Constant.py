import numpy as np
import matplotlib.pyplot as plt

# Step 1 - Function to calculate the madelung constant.
inp = int(input("You wish to calculate the madelung constant using how many terms of the series "))
sum = 0
def madelung_constant(n):
	if n >= 1:
		global sum
		sum += (-2*((-1)**n))/n 
		if n > 1:
			return madelung_constant(n-1)
		else:
			return sum
	elif n == 0: 
		return "Error, n must be >= 1."
	else:
		return "how did you get here, go back and give me a natural number"


# Step 2 - Plotting the convergence of the madelung constant. 
list_ind = list(range(inp))
mod_list = list(range(1, inp+1))

for i in list_ind:
	sum = 0 # Sum was global so that the madelung constant could be set to 0 and calculated in Step 1. Here it needs to be reset again for every i so that we're not 
	a = madelung_constant(i+1)
	mod_list[i] = a

# Aesthetics

title_font = {'text.usetex': True,
		'family': 'AppleGothic',
		'color': 'black',
		'size': '14',
		}
Axis_title_font = {'family': 'AppleGothic',
		'color': 'black',
		'size': '12',
		}
Legend_text = {'family': 'Times New Roman',
			   'color': 'black',
			   'size':'10'
		}

# Setting up Arrays
y = np.array(mod_list)
x = np.array(list_ind)
fig, ax = plt.subplots()
line1 = ax.plot(x,y)
ax.set_xlabel("Number of terms used to calculate the madelung constant.",fontdict=Axis_title_font)
ax.set_ylabel("M", fontdict=Axis_title_font)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_title("Approximation of Madelung's Constant using M = -2" r"$\sum_{n=1}^{\infty} \frac{(-1)^n}{n}$")
plot_text = "As the number of terms used to \ncalculate the Madelung constant tends \nto infinity, the value computed for the \nconstant tends to approximately 1.38."
ax.text(0.7*max(x),1, plot_text, fontdict=Legend_text)
print(max(y))
plt.show()
