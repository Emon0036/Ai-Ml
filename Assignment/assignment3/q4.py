number = (4,5,6,7,8,6,4)


even = ()  #touple
odd = ()

for i in number:
    if(i% 2 == 0):
        even += (i,)
    else:
        odd += (i,)

print(even)
print(odd)    
