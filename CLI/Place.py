# This is the Place class.
from Petrinetobjects import Petrinetobject


class Place(Petrinetobject):
    """docstring for Place.
    Each place object has the following features.
    1. no.of tokens at current place.
    place name which is a parent property --> never bother.
    """

    def __init__(self,name, start):
        self.name = name
        self.tokens = start

    def get_values(self):
        print(self.tokens,self.get_name())

    def hasatleat(nin):
        return (self.tokens >= nin)

    def get_tokens():
        return self.tokens

    def set_tokens(value):
        self.tokens = value

    def add_tokens(amount):
        self.tokens += amount
