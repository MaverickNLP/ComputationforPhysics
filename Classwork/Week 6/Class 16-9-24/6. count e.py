user_inp = input("give me a string any string   ")
e = 0
for i in user_inp:
	if i == 'e':
		e += 1
	else: 
		print("no e")
if e > 0:
	print('You have', e, "e's")