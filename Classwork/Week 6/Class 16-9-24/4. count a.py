user_inp = input("Give string.   ")
a = 0
for i in user_inp:
	if i == 'a' or i=='A':
		a += 1
	else:
		print("no a here")
print(a)