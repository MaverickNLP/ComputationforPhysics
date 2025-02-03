import numpy as np
import matplotlib.pyplot as plt

# Step 1 - Recursive Function for the Fibonacci Sequence:
range_no = int(input("You'd like to calculate the ratios between consecutive fibonacci numbers upto?    ")) # Determines n(the number upto which we have to calculate the fibonacci sequence)
index_list_fib = tuple(range(range_no+1)) #Defines a tuple index_list which allows us to define a for loop for fib_list.
fib_list = list(range(1, range_no+2)) # Defines a list fib_list into which n+1 fibonacci numbers can be calculated.
def fibonacci(n):
	if n == 0:
		return 1 # Question calls for f(0) = 0, however that wouldn't work since we need ratios, and F(0), would yield F(1)/F(0) = Undefined (since we can't divide by 0)
	elif n == 1: 
		return 1 # Defines 1, 1, for the fib seq
	else:
		return fibonacci(n-1) + fibonacci(n-2) # Returns the other terms for the fib sequence

# Step 2 - Calculating and Storing Ratios of Consecutive Fibonacci Numbers:

index_list_ratio = tuple(range(range_no)) # Defines a tuple that allows us to define a for loop for fib_ratio_list.
fib_ratio_list = list(range(1, range_no+1)) # Defines a list into which we can insert the desired ratios of the fibonacci sequence.
for i in index_list_fib:
	fib_list[i] = fibonacci(i) #creates the required fibonacci sequence values. 
for i in index_list_ratio:
	fib_ratio_list[i] = (fib_list[i+1])/(fib_list[i]) # Creates the required ratios between fibonacci sequence values.

# Step 3 - Setting up Aesthetics

title_font = {'family': 'AppleGothic',
		'color': 'black',
		'size': '14',
		} # Font for the title of the graph.
Axis_title_font = {'family': 'AppleGothic',
		'color': 'black',
		'size': '12',
		} # Font for the axis titels of the graph
Legend_text = {'family': 'Times New Roman',
			   'color': 'black',
			   'size':'10'} # Font for the legend 


#Setting Up Arrays:

gr = (1+(np.sqrt(5)))/2 # Assignment statement where gr = the Golden Ratio
ones_array = (np.ones(range_no)) # Defining an array to plot the constant golden ratio.
gr_y = np.multiply(ones_array,gr)
y = np.array(fib_ratio_list) # Creates an array using the values in fib_ratio_list for plotting
x = np.array(index_list_ratio) # Creates an array using the values in index_list_ratio for plotting (This would happen "under the hood" anyway but it's good practice to convert to array anyway I think)

#Setting up the plot:
fig, ax = plt.subplots()
ax.plot(x,y) # Plots the ratios of consecutive fibonacci numbers against their index.
ax.plot(x, gr_y, linestyle = 'dashed') #Plots a constant at the value of the golden ratio 
ax.set_xlabel("n -1",fontdict=Axis_title_font)
plt.ylim([0, max(y)+1]) # It looks pleasing since the y values will be between 1 and 2 :)) 
plt.xlim([0, max(x)+0.4]) # Needed to extend the x axis to fit the "observation" and comments. 
plt.ylabel(r"$\frac{F(n+1)}{F(n)}$" " where F(x) is the xth fibonnaci number", fontdict=Axis_title_font)
plt.title( "Calculating the Golden Ratio using the limit of " r"$\frac{F(n+1)}{F(n)}$", fontdict = title_font) 
plot_text = 'As n - 1 tends to infinity' r"  $\frac{F(n+1)}{F(n)}$" '\ntends to the golden ratio'
plt.text(0.7*max(x),gr-0.4, plot_text, fontdict=Legend_text)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.legend(['Fibonacci Sequence Ratios', 'Golden Ratio(Constant)'])

plt.show()



# Additional Step (Won't run unless you close the graph), Step 4 - Ratio between Ratios and Golden Ratio (for comments on how the ratio tends 
# towards the golden value.) 
for i in index_list_ratio: 
	print((i, (fib_ratio_list[i]-gr_y[i])/gr_y[i])) #Percentage error (clearly decreasing after every summation, implying that the ratios between
	# consecutive numbers in the fibonacci sequence will inch towards the golden ratio value of (1 + sqrt(5))/2. 
