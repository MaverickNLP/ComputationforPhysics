a = input("So, you wish to find the sum of a Harmonic Series with terms of type 1/k, upto the term n = k, where n is a natural number. Well what is your n? :")
b = int(a)+1
if b <= 1:
	print("Please provide a natural number!")
	exit()
else:
	c = list(range(b))
	e = list(range(b))
c.pop(0)
e.pop()
for i in c:
	c[i-1] = 1/(int(c[i-1]))
d = 0
for i in e:
	d = d + c[i-1] 
print(d)