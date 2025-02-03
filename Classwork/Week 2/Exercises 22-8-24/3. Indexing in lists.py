# you can extract the ith element of the list by printing listname[i] 
# elements are counted from 0 in python, overflow is prevented, i.e. -1 will print the last element of a list, -2 will print the second to last element and so on.
alist = [1,3,5,7,9]
blist = alist[0:2]
print(blist)
#printing some elements of lists by defining alist[a:b], will print elements a+1 to b-1. 

# If you want to print every nth element then alist[a:b:n] would yield every nth element of the lsit
alist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(alist[1:10:2])


# If no value is defined at start or stop then it defaults to starting at the beginning and stopping at the end. 
# Um no to the exercises 
print(alist[3:7])
# 1. Prints the 3rd to the 6th element, inclusive. 
print(alist[7:3])
# 2. Prints the 7th to the 2nd element, inclusive. I assume, let's check:
print(alist[7:3:-1])
# It prints nothing actually. Wow. Default step might be 1. So it just kills itself. 
# 3. Adding a - step to the list makes it work. 
print(alist[-1])
# 4. prints the last element
print(alist[3:])
# 5. Prints the 3rd element to the last element. 
print(alist[:7])
# 6. Prints the 1st to the 6th element of the list. 
print(alist[:])
# 7. prints all the elements in the list.
print(alist[::2])
# 8. Prints all the elements of the list indexed with odd numbers. 
print(alist[::-1])
# 9. Prints everything from end to start. 