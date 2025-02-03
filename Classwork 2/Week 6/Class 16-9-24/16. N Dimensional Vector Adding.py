inp1 = input("Enter your first vector, please seperate components with spaces    ")
inp2 = input("Enter your second vector, please seperate components with spaces   ")

def Convert(string):
	string = list(string.split( ))
	string = [int(i) for i in string]
	return string
inp1 = Convert(inp1)
inp2 = Convert(inp2)
addition = list(range(len(inp1)))
for i in addition:
	addition[i] = inp1[i] + inp2[i]
print(addition)