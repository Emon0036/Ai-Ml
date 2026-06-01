#tuple immutable

tuple = (1,2,3,5,6,6,"abc",7.8)

print(tuple)

print(tuple[4:7])

#method
#--------

#.index -> return the first occurences value
occur = tuple.index(6)

print(occur)


totaloccourences = tuple.count(6)

print(totaloccourences) 

