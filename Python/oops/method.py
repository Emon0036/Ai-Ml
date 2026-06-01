class student:
    # def __int__(self):
    #     print("I am self method")

# atuomatic method
# self store every information of the object

    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa

# user define method

    def get_cgpa(self):
        return self.cgpa


stud1 = student("Emon",3.50)
stud2 = student("Rahman",3.80)
stud3 = student("Rakib",3.85)



print( f"student name is {stud1.name} and cgpa is {stud1.cgpa}") 
print(f"student name is {stud2.name} and cgpa is {stud2.cgpa}")
print(f"student name is {stud3.name} and cgpa is {stud3.cgpa}")

print(stud1.get_cgpa())

