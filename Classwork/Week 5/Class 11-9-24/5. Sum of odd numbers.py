list_oddsum = list(range(1, 101, 1))
sum = 0
for i in list_oddsum:
	if i%2 == 0:
		continue
	elif i%2 == 1:
		sum += i

print(sum)