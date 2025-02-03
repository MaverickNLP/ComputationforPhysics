inp1 = float(input("type num bro   "))
inp3 = input("which operation do you want to perform (+, -,	*, /)?   ")
inp2 = float(input("type num bro   "))

result = 0
if inp3 == '+':
	result = inp1 + inp2
	print(result)
elif inp3 == '-':
	result = inp1 - inp2
	print(result)
elif inp3 == '*':
	result = inp1 * inp2
	print(result)
elif inp3 == '/':
	result = inp1/inp2
	print(result)
else:
	"loser please give me numbers and an operation"

