from product import Product
from electrical import Electrical
from product import positive_number_validator


class Laptop(Electrical, Product):
    def __init__(self, id, name, price, voltage, cpu, ram):
        self.id = id
        self.name = name
        self.price = price
        self.voltage = voltage
        self.cpu = cpu
        self.ram = ram

    @property
    def cpu(self):
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        self._cpu = positive_number_validator(cpu, "Invalid CPU")

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, ram):
        self._ram = positive_number_validator(ram, "Invalid RAM")
