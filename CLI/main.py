from Arc import Arc
from Transition import Transition
from Place import Place
from Petrinet import Petrinet
import sys
p = Petrinet() # creaating a petrinet obj.

no_of_places = int(input('Enter the no.of Places: '))

for i in range(no_of_places):
    name = input('Enter name for place: ')
    no_of_tokens = int(input('Enter no.of tokens in the initial position.'))
    tmp_place = Place(name,no_of_tokens)
    p.add_place(tmp_place)

no_of_transitions = int(input('Enetr the no.of Transitions: '))

for i in range(no_of_transitions):
    name = input('Enter name for Transition: ')
    tmp_transition = Transition(name)
    p.add_transition(tmp_transition)

no_of_arcs = int(input('Enter the no.of Arcs: '))
print('Enter all Arcs in [from index] (space delimiter) [to index] (space delimiter) [status (input/output)])')
for i in range(no_of_arcs):
    name = input('Enter name for Arc: ')
    tmp_arc = Arc(name)
    arc_details = input('Enter from, to, status: ')
    tmp_arc_details = arc_details.split()
    if tmp_arc_details[2] != 'input' and tmp_arc_details[2] != 'output':
        print("-------------------Wrong Input-----------------------------")
        sys.exit(0)
    else:
        if tmp_arc_details[2] == 'input':
            tmp_arc.initialize(p.places[int(tmp_arc_details[0])],p.transitions[int(tmp_arc_details[1])],tmp_arc_details[2])
            p.transitions[int(tmp_arc_details[1])].add_arc(tmp_arc)
        else:
            tmp_arc.initialize(p.transitions[int(tmp_arc_details[0])],p.places[int(tmp_arc_details[1])],tmp_arc_details[2])
            p.transitions[int(tmp_arc_details[0])].add_arc(tmp_arc)
        p.add_arc(tmp_arc)
p.reachability_graph()
