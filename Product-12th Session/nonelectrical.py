from product import Product, positive_number_validator


# product: id, name, price
class Nonelectrical(Product):
    def __init__(self, id, name, price, weight):
        super().__init__(id, name, price)
        self.id = id
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = positive_number_validator(weight, "Invalid Weight")
