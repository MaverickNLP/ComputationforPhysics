# A dictionary is a set but it's entries are strings and not int or float.
my_dict = {'name' : 'Alice', 'age':25, 'city':'new york'}
print(my_dict)
# If key values have pairs then all elements in a dictionary must be paired.
print(my_dict['name'])
# The order of brackets is important in Python 
my_dict['age']=26
print(my_dict) 
# You can access and modify the value as usual. You can also add a key pair like this 
my_dict['email'] = 'alice@example.com'
#Pairs are added to the end of the dictionary
del my_dict['city']
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
# Keys, prints the first set, i.e. the input that correlates to our output
# Values, prints the second set, i.e. the output that correlates to some input
# Items, prints out the key values, seperated by commas. 