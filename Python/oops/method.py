class student:
    department = "CSE"
    floor = 0
    # def __int__(self):
    #     print("I am self method")

# atuomatic method
# self -> store every information of the object

    def __init__(self,name,cgpa):   #instance method
        self.name = name
        self.cgpa = cgpa

# user define method

    def get_cgpa(self):   #instance method
        return self.cgpa
    

    # Class method
    @classmethod  #decorator
    def class_method(cls , floor):
        cls.floor = floor
        print(f"Department is:{cls.department}  {cls.floor}")

    #static method
    @staticmethod #it's a random function
    def calculate_pass(mark , pass_mark):
        if(mark > pass_mark):
            print(f"You have passed the exam")
            


stud1 = student("Emon",3.50)
stud2 = student("Rahman",3.80)
stud3 = student("Rakib",3.85)

stud1.class_method(5)



print( f"student name is {stud1.name} and cgpa is {stud1.cgpa}") 
print(f"student name is {stud2.name} and cgpa is {stud2.cgpa}")
print(f"student name is {stud3.name} and cgpa is {stud3.cgpa}")

print(stud1.get_cgpa())
stud1.calculate_pass(60 , 55)

