from Arc import Arc
from Transition import Transition
from place2 import Place2
from tokenslist import Tokenslist

n = 6
m = 6
k = 12
placeslst = []
transitionlst = []
Incoming = [[1,1,0,0,0,0],[0,0,1,1,0,0],[0,0,0,0,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
Outgoing = [[0,0,0,0,0,0],[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,1,0],[0,0,0,0,0,1]]
tokens = [1,0,0,0,0,0] # initial input of tokens.
t = Tokenslist(tokens)
for i in range(n):
    placeslst.append(Place2(i))
for i in range(m):
    transitionlst.append(Transition(i))
k = 0
for i in range(n):
    for j in range(m):
        if Incoming[i][j] == 1:
            temp = Arc(k)
            k += 1
            temp.initialize(i,j,0)
            transitionlst[j].add_arc(temp)
for i in range(n):
    for j in range(m):
        if Outgoing[i][j] == 1:
            temp = Arc(k)
            temp.initialize(i,j,1)
            transitionlst[j].add_arc(temp)
# for i in range(6):
#     transitionlst[i].describe()

# possible = []
# for i in range(6):
#     if transitionlst[i].can_fire(t):
#         possible.append(i)
# print(possible)
queue = [t]
dict = []

while queue:
    present = queue.pop(0)
    if present.lst not in dict: # this should be optimised with dictionary and need to store parents id in a list (because we can have more than one parent)
        dict.append(present.lst)
    # never going to change or touch present.
    for i in range(m):
        if transitionlst[i].can_fire(present):
            tmptoken = Tokenslist(present.lst)
            transitionlst[i].fire(tmptoken)
            queue.append(tmptoken)
print(dict)
