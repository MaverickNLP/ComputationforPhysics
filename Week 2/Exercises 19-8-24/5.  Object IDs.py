a = 3.14
b = 3.14
c = 3.14 
d = "Hello"
e = "Hello"

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
# Q a) variables with the same value are stored at the same location
# locations are always changing 
# Q b) The ids of the locations are always chagning and it seems to prefer 43________ however there's a line where I got a 44. 
# Floats with the same value in VSC are stored at the same location. On Jupyter, Kripa got a different result. Could she be running an earlier version of python? Is this a thing in Jupyter??? Only the Python gods know.