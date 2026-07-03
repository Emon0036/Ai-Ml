class laptop:
    storage_type = "ssd"



    def __init__(self,ram , storage):
        self.ram = ram
        self.storage = storage

    def __init__(self):
            print("Hello I am the second one")

    def get_info(self):
        print(f"laptop has {self.ram}gb Ram , {self.storage}gb storage")


obj1 = laptop()

