a = True
b = False 
c = True

print(not ((a or b) and c))
print((not a and not b) or (not c))

print(not(a and (not b)) or c)
print((not a or b)or c)