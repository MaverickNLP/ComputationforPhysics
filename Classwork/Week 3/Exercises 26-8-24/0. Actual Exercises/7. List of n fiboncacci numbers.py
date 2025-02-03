a = int(input("How many fibonacci numbers do you need?  "))
b = [1]
if a == 1: 
	print(b)
else:
	f = [1,1]
	c = list(range(a-2))
	for i in c:
		f.append(0)
	for i in c:
		f[i+2]=f[i]+f[i+1]
	print(f)