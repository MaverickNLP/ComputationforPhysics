a = input("So, you wish to find the sum of a Harmonic Series with terms of type [(-1)**(k+1)]/k, upto the term n = k, where n is a natural number. Well what is your n? :")
b = int(a)+1
if b <= 1:
	print("Please provide a natural number!")
	exit()
else:
	c = list(range(b))
	e = list(range(b))
f = []
for i in c:
	f.append((-1)**i)
c.pop(0)
e.pop()
d = []
for i in e:
	c[i] = 1/(c[i]*f[i])
g = 0
for i in e:
	g = g + c[i]
print(g)