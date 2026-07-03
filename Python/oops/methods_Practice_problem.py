class Product:
    count = 0
    def __init__(self,name , price):
        self.name = name
        self.price = price
        Product.count += 1
      #instanse method    
    def print_product(self):
        print(f"Name:{self.name} {self.price}")  

    @classmethod
    def get_count(cls):
        print(f"total count:{cls.count}")

    @staticmethod
    def calc_discount(price , discount):
        main_pirce = price - (price * discount/100)
       # print(f"discounted price = { main_pirce}") 
        return main_pirce       

products = []
discount_price = []
n = int(input("Enter how many input you want to enter:"))

# To give input
for i in range(1 , n+1 ,1):
    print(f"\nEnter the entry number: {i}")

    name = input("Enter the product name:")
    price = float(input("Enter the product price:"))

    product = Product(name,price) # creat an object
    products.append(product)

# To give input the percentage
for i in range(1 , n+1 ,1):
    print(f"\nEnter the entry number: {i}")

    P_price = int(input("Enter the product Price:"))
    discount = int(input("Enter the product discount in percentage(%):"))

    r_price= product.calc_discount(P_price,discount) 
    discount_price.append(r_price)
       

for product in products:
    print(product.print_product()) 

for price ,product in zip(discount_price , products):  
    print(f"After discount the price of {product.name} is {price}")     

Product.get_count()   
       