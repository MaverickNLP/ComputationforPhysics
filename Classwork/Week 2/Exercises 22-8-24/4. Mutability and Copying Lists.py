alist=[1,3,5,7,9,11,13,15,17,19]
alist[2] = 'five'
print(alist)
# Lists are mutable, i.e. an indexed element can be changed as shown above. 

alist=[1,3,5,7,9,11,13,15,17,19]
blist = alist
alist[3]='seven'
print(blist)
# If alist = blist and an element in alist is changed after defining so, blist's element will change too. 
# This happens since alist and blist are stored in the same location. 
# To make a copy that is seperately mutable we need to specify that the new list contains all elements of the old list but not the 