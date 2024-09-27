from product import Product, positive_number_validator


class Electrical(Product):
    def __init__(self, id, name, price, voltage):
        super().__init__(id, name, price)
        self.id = id
        self.name = name
        self.price = price
        self.voltage = voltage

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = positive_number_validator(voltage, "Invalid Voltage")
