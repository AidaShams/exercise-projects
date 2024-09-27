import re


def validator(variable, regex_pattern, error_message):
    if type(variable) == str and re.match(regex_pattern, variable):
        return variable
    else:
        raise ValueError(error_message)


def positive_number_validator(variable, error_message):
    if type(variable) == float and variable >= 0:
        return variable
    else:
        raise ValueError(error_message)


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = positive_number_validator(id, "Invalid ID")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = validator(name, r"^[a-zA-Z\s]{2,20}$", "Invalid Name")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = positive_number_validator(price, "Invalid Price")