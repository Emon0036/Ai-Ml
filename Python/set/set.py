#set->it stores the unique element

set ={1,2,3,4,5,6,5,5,5}

print(set)
print(len(set))
print(type(set))

#method

set.add(78)
print(set)


set.remove(5)

print(set)

set.clear()

print(set)

set1={4,5,6,7,8,2,4}
set2={8,7,6,5,4,3,6}

print(set1.pop())
print(set1.pop())


print(set1.union(set2))

print(set1.intersection(set2))