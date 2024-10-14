from product import Product
from nonelectrical import Nonelectrical
from product import positive_number_validator


class Furniture(Nonelectrical, Product):
    def __init__(self, id, name, price, weight, capacity):
        self.id = id
        self.name = name
        self.price = price
        self.weight = weight
        self.capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = positive_number_validator(capacity, "Invalid Capacity")
