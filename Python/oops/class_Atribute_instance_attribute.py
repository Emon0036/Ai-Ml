class student:
    subject = "Python"

    def __init__(self,name , cgpa , subject):
        self.name = name
        self.cgpa = cgpa
        self.subject = subject
        
# there are 2 same name attribute but priority goes to the instance attribute

st1 = student("Emon" , 3.60,"Javascript")

print(f"The name is {st1.name} , cgpa {st1.cgpa} and {st1.subject}")
