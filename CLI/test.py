from Arc import Arc
from Transition import Transition
from Place import Place
from tokenslist import Tokenslist
from Petrinet import Petrinet
# n = 6
# m = 6
# k = 12
# placeslst = []
# transitionlst = []
# Incoming = [[1,1,0,0,0,0],[0,0,1,1,0,0],[0,0,0,0,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
# Outgoing = [[0,0,0,0,0,0],[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,1,0],[0,0,0,0,0,1]]
# tokens = [1,0,0,0,0,0] # initial input of tokens.
# t = Tokenslist(tokens)
# for i in range(n):
#     placeslst.append(Place2(i))
# for i in range(m):
#     transitionlst.append(Transition(i))
# k = 0
# for i in range(n):
#     for j in range(m):
#         if Incoming[i][j] == 1:
#             temp = Arc(k)
#             k += 1
#             temp.initialize(i,j,0)
#             transitionlst[j].add_arc(temp)
# for i in range(n):
#     for j in range(m):
#         if Outgoing[i][j] == 1:
#             temp = Arc(k)
#             temp.initialize(i,j,1)
#             transitionlst[j].add_arc(temp)
# # for i in range(6):
# #     transitionlst[i].describe()
#
# # possible = []
# # for i in range(6):
# #     if transitionlst[i].can_fire(t):
# #         possible.append(i)
# # print(possible)
# queue = [t]
# dict = []
#
# while queue:
#     present = queue.pop(0)
#     if present.lst not in dict: # this should be optimised with dictionary and need to store parents id in a list (because we can have more than one parent)
#         dict.append(present.lst)
#     # never going to change or touch present.
#     for i in range(m):
#         if transitionlst[i].can_fire(present):
#             tmptoken = Tokenslist(present.lst)
#             transitionlst[i].fire(tmptoken)
#             queue.append(tmptoken)
# print(dict)

p1 = Place("P1",1)
t1 = Transition("T1")
a1 = Arc("A1")
a1.initialize(p1,t1,"input")
t1.add_arc(a1)
p2 = Place("P2",0)
p3 = Place("P3",0)
p4 = Place("P4",0)
p5 = Place("P5",0)
p6 = Place("P6",0)
p7 = Place("P7",0)
p8 = Place("P8",0)
t2 = Transition("T2")
t3 = Transition("T3")
t4 = Transition("T4")
t5 = Transition("T5")
a2 = Arc("A2")
a2.initialize(t1,p2,"output")
t1.add_arc(a2)
a3 = Arc("A3")
a3.initialize(t1,p3,"output")
t1.add_arc(a3)
a4 = Arc("A4")
a4.initialize(p2,t2,"input")
t2.add_arc(a4)
a5 = Arc("A5")
a5.initialize(p3,t2,"input")
t2.add_arc(a5)
a6 = Arc("A6")
a6.initialize(p3,t3,"input")
t3.add_arc(a6)
a7 = Arc("A7")
a7.initialize(t2,p4,"output")
t2.add_arc(a7)
a8 = Arc("A8")
a8.initialize(t3,p4,"output")
t3.add_arc(a8)
a9 = Arc("A9")
a9.initialize(t3,p5,"output")
t3.add_arc(a9)
a10 = Arc("A10")
a10.initialize(t3,p6,"output")
t3.add_arc(a10)
a11 = Arc("A11")
a11.initialize(p4,t4,"input")
t4.add_arc(a11)
a12 = Arc("A12")
a12.initialize(p5,t4,"input")
t4.add_arc(a12)
a13 = Arc("A13")
a13.initialize(p5,t5,"input")
t5.add_arc(a13)
a14 = Arc("A14")
a14.initialize(p6,t5,"input")
t5.add_arc(a14)
a15 = Arc("A15")
a15.initialize(t4,p7,"output")
t4.add_arc(a15)
a16 = Arc("A16")
a16.initialize(t5,p8,"output")
t5.add_arc(a16)

p = Petrinet()
p.add_place(p1)
p.add_place(p2)
p.add_place(p3)
p.add_place(p4)
p.add_place(p5)
p.add_place(p6)
p.add_place(p7)
p.add_place(p8)
p.add_arc(a1)
p.add_arc(a2)
p.add_arc(a3)
p.add_arc(a4)

p.add_arc(a5)
p.add_arc(a6)
p.add_arc(a7)
p.add_arc(a8)

p.add_arc(a9)
p.add_arc(a10)
p.add_arc(a11)
p.add_arc(a12)

p.add_arc(a13)
p.add_arc(a14)
p.add_arc(a15)
p.add_arc(a16)

p.add_transition(t1)
p.add_transition(t2)
p.add_transition(t3)
p.add_transition(t4)
p.add_transition(t5)
p.reachability_graph()
