#list like array (mutable)
list = [22,25,36,"Emon",67.90]

print(list)

# list[1] = 45

# print(list)

# for i in list:
#     print(i,end=" ")

#method

#add value at the last
list.append(90)

#insert -> insert value at any position.Shif the value from that place 

list.insert(1,67)
print(list)

#sort()-> sort value at ascending order

num = [24,56,67,89,90,65]

num.sort()

print(num)

#reverse=True it means reverse the number into descending order
num.sort(reverse=True)

print(num)


# reverse() -> help us to reverse the whole list

list.reverse()
print(list)

