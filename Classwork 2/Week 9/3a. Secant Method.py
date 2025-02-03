def f(x):
	return x**2-5

x0 = 1 
x1 = 2
tol = 0.01
diff = 1
while diff > tol:
	print(x0)
	x2 = x1 - (f(x1))*((x1-x0)/(f(x1)-f(x0))) 
	x0 = x1
	x1 = x2
	if x0 == x1:
		exit()
print(x1)