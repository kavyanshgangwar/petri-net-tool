# This is the Place class.
from Petrinetobjects import Petrinetobject


class Place2(Petrinetobject):
    """docstring for Place.
    Each place object has the following features.
    1. no.of tokens at current place.
    place name which is a parent property --> never bother.
    """

    def __init__(self,name):
        self.name = name
