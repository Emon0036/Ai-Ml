
a = 4
b = 5

sum = a + b

# format
#-----------------
print("sum of the values {}".format(sum))

print("sum of  {} & {} are {}".format(a,b,sum))

print("My name is {}".format("Emon Rahman"))


# index based formating
print("sum of  {1} & {0} are {2}".format(a,b,sum))

# value based formating

print("sum of  {a} & {b} is {c}".format(a=5,b=6,c=a+b))


# f-string {python(3.6)}
#------------------------

print(f"sum of {a} & {b} is {sum}")

print(f"sum of {5} & {6} is {5 + 6}")