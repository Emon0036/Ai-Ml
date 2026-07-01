
def hello():
    print("Hello")
    print("Hello from python")


hello() #non-perametarise function



def sum(a , b):
    sum = a + b

    return sum

sum = sum(5,6)
print(sum)


# lamda function
avg = lambda a,b,c: (a+b+c)/3

print(avg(7,8,9))


# calculate N factorial

def factorial(n):
         
         fact = 1

         for i in range(1 , n+1 , 1):
               fact *=i
         return fact


fact = factorial(5)

print(fact)