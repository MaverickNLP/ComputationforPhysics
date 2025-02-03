import random as rand
N = int(input("You'd like me to guess a random integer between 0 and?    "))
a = int(N/2)
b = int(input("What's the number that you'd like me to guess?   "))
list_bound = [0, N]
tries = 0
list_tries = []



while b != a:
	if b >= a:
		print("Ah my guess of", a, "was lower than your value, let me try again!", print(list_bound))
		list_bound[0] = a
		a = int((list_bound[0] + list_bound[1])/2)
		tries += 1
		list_tries.append(a)
	if b <= a: 
		print("Ah my guess of", a, "was higher than your value, let me try again!", print(list_bound))
		list_bound[1] = a
		a = int((list_bound[0] + list_bound[1])/2)
		tries += 1
		list_tries.append(a)
	elif a == b:
		tries += 1 
		print("Yay", a, "was your number.", "and I got it in", tries, "tries")
	elif a in list_tries:
		a += 1
		tries += 1
		list_tries.append(a)
		print("I must guess with += 1 now, unfortunately, therefore I guess", a)
