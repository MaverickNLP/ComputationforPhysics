a = list(range(0, 10, 2))
b = list(range(1, 11, 2))
c = []
for i in a: 
	c.append(0)
for i in b: 
	c.append(0)
c[0:10:2] = a
c[1::2] = b
print(c)
# inverse a and b position if you need to change the order. 