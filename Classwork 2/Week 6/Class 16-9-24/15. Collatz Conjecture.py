a = int(input("you'd like to start the collatz conjecture at   "))
step =0
while a != 1:
	step += 1
	if a%2 == 0:
		a = a/2
		print(step, int(a))
	elif a%2 == 1:
		a = (3*a+1)/2
		print(step, int(a))