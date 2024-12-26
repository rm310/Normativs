from abc import ABC, abstractmethod

class Computer(ABC):
    __total_computers = 0
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price = price
        Computer.__total_computers += 1

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if not value:
            raise ValueError("price can not be empty")
        if value < 0:
            raise ValueError("price should be more than 0")
        self.__price = value

    def __gt__(self,y):
        return self.__price > y.price

    @classmethod
    def get_total_comp(cls):
        return cls.__total_computers

    @abstractmethod
    def display_info(self):
        pass

class Factory:
    count = 0
    def __init__(self):
        self.computers = []
    def add_computer(self, computer: Computer):
        if isinstance(computer, Computer):
            self.computers.append(computer)
            print("Computer qoshildi")
        else:
            print("Kiritilgan malumot notogri")

    def list_computers(self):
        for computer in self.computers:
            print(computer.display_info())

    @classmethod
    def get_count(cls):
        return cls.__total_computers


class Monoblock(Computer):
    def __init__(self, brand, model, year, price, screen_size):
        super().__init__(brand, model, year, price)
        self.screen_size = screen_size

    def display_info(self):
        return (f"Brand: {self.brand}, \n"
                f"Model: {self.model}, \n"
                f"Year: {self.year}, \n"
                f"Price: {self.price}, \n"
                f"Screen size: {self.screen_size}, \n")



class Notebook(Computer):
    def __init__(self, brand, model, year, price, battery_life):
        super().__init__(brand, model, year, price)
        self.battery_life = battery_life

    def display_info(self):
        return (f"Brand: {self.brand}, \n"
                f"Model: {self.model}, \n"
                f"Year: {self.year}, \n"
                f"Price: {self.price}, \n"
                f"Battery life: {self.battery_life}, \n")

notebook1 = Notebook("a", "b", 21, 23.000, 2)
notebook2 = Notebook("b", "f", 23, 34.222, 3)
print(notebook1.display_info())
print(notebook2.display_info())

monoblock1 = Monoblock("c", "v", 23, 34.555, "1234x3456")
monoblock2 = Monoblock("d", "w", 12, 34.112, "3452x4376")
print(monoblock1.display_info())
print(monoblock2.display_info())


factory = Factory()
factory.add_computer(notebook1)
factory.add_computer(notebook1)
factory.add_computer(monoblock1)
factory.add_computer(monoblock2)
print()

factory.list_computers()

print("Total computers: ", monoblock2.get_total_comp())
print(f"{monoblock1.model} ni narxi {monoblock2.model} dan koproqmi? -", monoblock1 > monoblock2) # __gt__ uchun


