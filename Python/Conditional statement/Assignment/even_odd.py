
def check(start , end):
    for i in range(start , end):
        if(i % 2 == 0):
            print(i)

    

a = int(input("Enter number a:"))
b = int(input("Enter number b:"))

print(check(a,b))
