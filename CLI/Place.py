# This is the Place class.



class Place:
    """docstring for Place.
    Each place object has the following features.
    1. no.of tokens at current place.
    place name which is a parent property --> never bother.
    """

    def __init__(self,name, start):
        self.name = name
        self.tokens = start

    def get_values(self):
        print(self.get_name()+" "+str(self.tokens))

    def hasatleast(self,nin):
        return (self.tokens >= nin)

    def get_tokens(self):
        return self.tokens

    def set_tokens(self,value):
        self.tokens = value

    def add_tokens(self,amount):
        self.tokens += amount

    def __str__(self):
        return self.name
