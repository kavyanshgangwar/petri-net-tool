# base class for all petrinet classes.

class Petrinetobject(object):
    """docstring for Petrinetobject."""
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
