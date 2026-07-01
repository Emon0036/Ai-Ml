salary = int(input("Enter your salary:"))

if(salary < 30000):
    print("Your tax rate is:",(salary + (salary*0.05)))
elif(salary >= 30000 and salary <=70000):
      print("Your tax rate is:",(salary + (salary*1.5)))  

elif(salary>70000):
       print("Your tax rate is:",(salary + (salary*2.5)))