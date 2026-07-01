def sum_of_the_digit(a):
    sum = 0
    while(a != 0):
        rem = a % 10
        sum += rem
        a = a//10
    return sum   

  


num = int(input("Enter the number:"))
print(sum_of_the_digit(num))