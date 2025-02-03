a = input("How many 1s of how many 1s do you wish to generate?    ")
b = int(a)+1
if b <= 1:
	print("Please provide a natural number!")
	exit()
else:
	c = list(range(b))
	d = []
	for i in c:
		d.append([1]*i)
	d.pop(0)
	print(d)