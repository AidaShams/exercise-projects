from electrical import Electrical
from product import Product
from product import validator


class Phone(Electrical, Product):
    def __init__(self, id, name, price, voltage, size):
        self.id = id
        self.name = name
        self.price = price
        self.voltage = voltage
        self.size = size

    @property
    def size(self):
        return

    @size.setter
    def size(self, size):
        self._size = validator(size, r"^[0-9]{3}x[0-9]{3}$", "Error! ex:200x300")
