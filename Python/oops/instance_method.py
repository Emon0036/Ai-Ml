class laptop:
    storage_type = "ssd"

    def __init__(self,ram , storage):
        self.ram = ram
        self.storage = storage

    def get_info(self):
        print(f"laptop has {ram}gb Ram , {storage}gb storage")