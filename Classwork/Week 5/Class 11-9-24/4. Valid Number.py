check_range = list(range(1,11))
input1 = float(input("Please give me an integer between 1 and 10.   "))
while input1 not in check_range:
	input1 = float(input("Please give me an integer between 1 and 10.   "))
