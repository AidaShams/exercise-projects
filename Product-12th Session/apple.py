from phone import Phone
from electrical import Electrical
from product import Product
from product import validator


class Apple(Product, Electrical, Phone):
    def __init__(self, id, name, price, voltage, size, country):
        self.id = id
        self.name = name
        self.price = price
        self.voltage = voltage
        self.size = size
        self.country = country

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = validator(country, r"^[a-zA-Z\s]{2,20}$", "Invalid Country")
