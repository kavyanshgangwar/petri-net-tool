from Petrinetobjects import Petrinetobject
from Arc import Arc
from tokenslist import Tokenslist

class Transition(Petrinetobject):
    """docstring for Transition."""

    def __init__(self,name,nin=1):
        self.name = name
        self.nin = nin
        self.incoming_arcs = []
        self.outgoing_arcs =[]

    def can_fire(self,tokenslistobj):
        can = True
        for arc in self.incoming_arcs:
            can = can & tokenslistobj.hasatleast(arc.place,self.nin)
        return can;

    def fire(self,tokenslistobj):
        for arc in self.incoming_arcs:
            tokenslistobj.alter_tokens_at_place(arc.place,-self.nin)
        for arc in self.outgoing_arcs:
            tokenslistobj.alter_tokens_at_place(arc.place,self.nin)

    def add_arc(self,arc):
        if arc.status == 0:
            self.incoming_arcs.append(arc)
        else:
            self.outgoing_arcs.append(arc)
    def describe(self):
        print("name :-",self.name)
        print("incoming arcs")
        for arc in self.incoming_arcs:
            print("arc Place",arc.place)
            print("arc transition",arc.transition)
        print("Outgoing arcs")
        for arc in self.outgoing_arcs:
            print("arc Place",arc.place)
            print("arc transition",arc.transition)
