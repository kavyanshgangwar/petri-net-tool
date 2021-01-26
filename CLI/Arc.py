# class for arcs
from Petrinetobjects import Petrinetobject

class Arc(object):
    """docstring for Arc."""

    def __init__(self, name):
        self.name = name
    def initialize(self,place_name,transition_name,status):
        self.place = place_name
        self.transition = transition_name
        self.status = status
