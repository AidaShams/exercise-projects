from phone import Phone
from electrical import Electrical
from product import Product


class Samsung(Product, Electrical, Phone):
    def __init__(self, id, name, price, voltage, size, flip):
        self.id = id
        self.name = name
        self.price = price
        self.voltage = voltage
        self.size = size
        self.flip = flip

    @property
    def flip(self):
        return self._flip

    @flip.setter
    def flip(self, flip):
        self._flip = flip
        if flip:
            return True, "Is Flip"
        else:
            return True, "Is Not Flip"
