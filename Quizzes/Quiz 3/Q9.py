import matplotlib.pyplot as plt
def f(x):
	return 3/(2*x) - x/2
def f_dash(x):
	return (-3/2)/(x**2)-1/2
def g(x):
	return (1/2)* (x+3/x)
list_y = [1]
iteration_limit = list(range(100))
list_x = [1]
# Apply Newton's method to f(x) to find fixed point of g(x)
for i in iteration_limit:
	yO = list_y[-1]
	y1 = yO - f(yO)/f_dash(yO)
	x0 = list_x[-1]
	x1 = x0 + 1
	list_y.append(y1) # Woops wrong list, I think extend takes a list as an argument and append must take an element. Welp.
	list_x.append(x1)
line1 = plt.plot(list_x, list_y)
plt.show()