
def check_plaindrome(name):
    temp = name[::-1]

    if(name == temp):
        print(f"{name} is plaindrome")
    else:
        print(f"{name} is not plaindrome")   


name = input("Enter a Name:")
check_plaindrome(name)