list1 = ['Monday', 'Tuesday', 'Wednesday']
list2 = ['apples', 'oranges']
print(list1+list2)
print(list2+list1)
# Order of addition matters. 

print(3*list1, list2*(-1))
#list 2 into -1 yields a null set, N * list yields that list repeated N times. 

# 3 list 1s will be printed 
# list 2 and list 1 will be printed together, as if they were a single list, however their elements would be seperated by a rectangular bracket 
# list 1 would be printed twice as if they were in the same list

print(3*list1+(-1)*list2)
print([list2]+[list1])
print(list1 + [list1])