from Petrinetobjects import Petrinetobject

class Transition(Petrinetobject):
    """docstring for Transition."""

    def __init__(self,name):
        self.name = name
    incoming_arcs = []
    outgoing_arcs =[]

    def can_fire():
        can = True
        for arc in self.incoming_arcs:
            can = can & arc.can_fire()
        return can;

    def fire():
        for arc in self.incoming_arcs:
            arc.fire()
        for arc in self.outgoing_arcs:
            arc.fire()
    def add_arc(arc,status):
        if status == 0:
            self.incoming_arcs.append(arc)
        else:
            self.outgoing_arcs.append(arc)
