class Gadget:
    # TODO: Modify the constructor to also accept a price parameter and initialize it using the setter method
    def __init__(self, name,price):
        self.__name = name
        self.__price = self.set_price(price)
        #self.set_price(price)
        

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    # TODO: Add set_price method with a condition to ensure the price is not set below 50.00, if so, set it to 50.00
    def set_price(self,price):
        if price >=50:
            self.__price = price
        else:
            self.__price = 50

    # TODO: Add get_price method
    def get_price(self):
        return self.__price

gadget = Gadget("Smartphone", 999.99)
gadget.set_name("Laptop")
# TODO: Set the price to 49.99
gadget.set_price(49.99)
print("Name:", gadget.get_name())

# TODO: Print the price
print(f"{gadget.get_price()}")
