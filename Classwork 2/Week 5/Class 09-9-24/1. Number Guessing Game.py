import random as rand
N = int(input("You'd like a random integer between 0 and?    "))
inp = int(input("What number do you think Python will choose?    "))
a = rand.randint(0, N)
tries = 0
while a != inp and N >= inp and 0 <= inp: 
	if a <= inp:
		print("Your guess was higher than the number I picked!")
		inp = int(input("Guess again!"   ))
		tries += 1
	elif a >= inp: 
		print("Your guess was lower than the number I picked!")
		inp = int(input("Guess again!"   ))
		tries += 1
	else:
		print("HOW DID YOU GET HERE LET ME KNOW @ kaushik.palavalasa24_ug@apu.edu.in")
if a == inp: 
	tries += 1
	print("Yeah that's right.", "You took", tries, "tries!")
