a = list(range(0,10,2))
b = list(range(1,11,2))
c = list(range(5))
d = []
for i in c: c[i] = (a[i]+b[i])
print(c)