from Arc import Arc
from Transition import Transition
from Place import Place
from Petrinet import Petrinet
from complete import Complete
import sys
p = Complete() # creaating a petrinet obj.

no_of_places = int(input('Enter the no.of Places: '))

for i in range(no_of_places):
    name = input('Enter name for place: ')
    no_of_tokens = int(input('Enter no.of tokens in the initial position.'))
    tmp_place = Place(name,no_of_tokens)
    p.add_place(tmp_place)

no_of_transitions = int(input('Enetr the no.of Transitions: '))

for i in range(no_of_transitions):
    name = input('Enter name for Transition: ')
    lb = int(input("Enter the lambda of transition: "))
    tmp_transition = Transition(name,lb)
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
print("The reachability graph is: ")
p.reachability_graph()

print("The Q matrix is: ")
p.find_q_matrix()

print("The pie vector is: ")
p.find_pie_vector()

for i in range(len(p.places)):
    print("The Mean no.of Tokens at place "+ p.places[i].name +" is : ")
    res = p.get_mean_tokens_place(p.places[1])
    print((res))

for i in range(len(p.transitions)):
    print("The Probability of firing transition "+p.transitions[i].name+" is:")
    res = p.probability_firing_trans(p.transitions[3])
    print(res)

for i in range(len(p.transitions)):
    print("The throughtput for transition "+p.transitions[i].name +" is:")
    res = p.Throughtput(p.transitions[3])
    print(res)
