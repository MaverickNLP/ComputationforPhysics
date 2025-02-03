a = range(50)
b = []
e = []
for i in a: 
	b.append(i*2)
	e.append(i*2+1)
c = range(100)
d = []
f = []
for i in a: 
	if b[i] == c[2*i]:
		d.append(1)
	if e[i] == c[2*i+1]:
		d.append(-1)
print(d)

#Kripa Sol
# a = list(range(100))
# b = []
# for i in a: 
# 	b.append((-1)**i)
# print(b)