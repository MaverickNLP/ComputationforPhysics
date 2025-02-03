def fct(n):
	if n < 2:
		return 1
	else: 
		return n * fct(n-1)
a = input("How many rows of the pascal's triangle do you wish to generate:    ")
b = int(a)+1
if b <= 1:
	print("Please provide a natural number!")
	exit()
else:
	c = list(range(b))
d = []
for i in c: 
	d.append(1)
	e = list(range(i+1))
	for j in e: 
		d[j] = int(fct(i)/(fct(i-j)*fct(j)))
	print(i, d)