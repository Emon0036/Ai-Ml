def count_num(a):
    count = 0
    while(a != 0):
        a = a//10
        count = count +1

    return count 


num = int(input("Enter the number:"))
print(count_num(num))