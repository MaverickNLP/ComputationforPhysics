User_input = input("Give me a word, make it a palindrome:")

rev_word = User_input[::-1]
if rev_word == User_input:
	print("That's a palindrome!")
else:
	print("That's not a palindrome!")