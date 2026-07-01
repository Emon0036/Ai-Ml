age = int(input("Enter your age:"))

if (age >= 18):
    print("You can vote")
elif (age>=10 and age <=15):
    print("You are in mid age you can't vote right now")
    print("You have to wait for a while")
else:
    print("you can't vote")
