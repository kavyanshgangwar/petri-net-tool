
from Arc import Arc
from tokenslist import Tokenslist

class Transition:
    """docstring for Transition."""

    def __init__(self,name,lb):
        self.name = name
        self.lambdai = lb
        self.incoming_arcs = []
        self.outgoing_arcs =[]

    def can_fire(self,state,placeindex):
        for arc in self.incoming_arcs:
            if state[placeindex[arc.frm]]==0:
                return False
        return True

    def fire(self,state,placeindex):
        l = []
        for x in state:
            l.append(x)
        for arc in self.incoming_arcs:
            l[placeindex[arc.frm]]=0
        for arc in self.outgoing_arcs:
            l[placeindex[arc.to]]=1
        return l

    def add_arc(self,arc):
        if arc.status == "input":
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

    def __str__(self):
        return self.name
