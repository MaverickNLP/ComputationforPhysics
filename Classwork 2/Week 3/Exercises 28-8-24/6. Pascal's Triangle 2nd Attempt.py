rows_string = int(input("How many rows of the pascal's triangle do you wish to generate:    "))
if type(rows_string) == int:
		print("Yay, give me a moment while I painstakingly calculate your Pascal's Triangle for you!")
row_id_list = list(range(1, rows_string+1)) #Defines the number of rows in the Pascal's Triangle that we want to print out.
index_tbmanipulate_list = []
for i in row_id_list:
	index_tbmanipulate_list= list(range(1, i-1))
	print(index_tbmanipulate_list)
	row = []
	
	