
class encapsulation:
    def __init__(self,name , money):
           self.name = name
           self.__money = money  # one (_) means protected but accessable but (__) means private (user1._encapsulation__money) in that way I can access this value
       
    # getter method
    def get_value(self):
          return self.__money
    
    # setter method
    def get_value(self):
          return self.__money

user1 = encapsulation("Emon" , 50000)

print(user1.name , user1.get_value())