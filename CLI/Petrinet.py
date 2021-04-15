"""
Have to input Petrinet(create).
push tokens list to the queue.
for each queue element explore all possible states generated and push them to queue should I store a rank,parents dictionary for each possible tokens vector.

More concise algo:-
step-1
genrate n places, m transitions, get all arcs for the petrinet,initial state for tokens.
Step-2
"""
from Place import Place
from Arc import Arc
from Transition import Transition
import numpy as np
class Petrinet:
    def __init__(self):
        self.places = []
        self.transitions = []
        self.arcs = []
        self.Q = []
        self.states = []

    # function for adding places
    def add_place(self,place):
        assert (type(place)==Place), "object is not of type Place."
        self.places.append(place)

    # function for adding arcs
    def add_arc(self, arc):
        assert (type(arc)==Arc), "object is not of type Arc."
        self.arcs.append(arc)

    # function for adding transition
    def add_transition(self, transition):
        assert (type(transition)==Transition), "object is not of type Transition."
        self.transitions.append(transition)

    # function for geting a dictionary mapping for palce and its corresponding index
    def get_palce_index_mapping(self):
        m = {}
        cur=0
        for place in self.places:
            if m.get(place) == None:
                m[place] = cur
                cur+=1
        return m

    # function to find the initial state of the graph
    def find_initial_state(self):
        n = len(self.places)
        s = [1 for x in range(n)]
        self.placeindex = self.get_palce_index_mapping()
        for arc in self.arcs:
            if arc.status == "output":
                if s[self.placeindex[arc.to]]==1:
                     s[self.placeindex[arc.to]]=0
        # s = [1,0,0,0,0]
        return s


    # helper function to find the reachability graph
    def find_reachability_graph(self):
        queue = []
        vis = []
        graph_edges = []
        queue.append(self.find_initial_state())
        while len(queue) != 0:
            u = queue.pop(0)
            if u in vis:
                continue
            else:
                vis.append(u)
            for transition in self.transitions:
                if transition.can_fire(u,self.placeindex):
                    v = transition.fire(u,self.placeindex)
                    graph_edges.append([u,v,transition])
                    if v not in vis:
                        queue.append(v)
        if len(self.states) == 0:
            self.states = vis[:]
        return graph_edges


    # function to find the reachability graph
    def reachability_graph(self):
        graph_edges = self.find_reachability_graph()
        self.print_graph(graph_edges)


    # function to print graph
    def print_graph(self,graph_edges):
        for edge in graph_edges:
            edge[0] = [str(x) for x in edge[0]]
            edge[1] = [str(x) for x in edge[1]]
            print("".join(edge[0])+" ---"+str(edge[2])+"---> "+"".join(edge[1]))

    def find_q_matrix(self):
        graph_edges = self.find_reachability_graph()
        q1 = [0 for i in self.states]
        self.q = [q1[:] for i in self.states]
        for edge in graph_edges:
            a=0
            b=0
            for i in range(len(self.states)):
                if edge[0] == self.states[i]:
                    a=i
                if edge[1] == self.states[i]:
                    b=i
            self.q[a][b] += edge[2].lambdai
        for i in range(len(self.states)):
            sm = 0
            for j in range(len(self.states)):
                sm+=self.q[i][j]
            self.q[i][i] = -1 * sm
        self.Q = (np.array(self.q)).T
        print(self.Q)
        eps = 1e-15
        u, s, vh = np.linalg.svd(self.Q)
        print(" s : \n", s)
        print("\nvh:\n",vh)
        null_space = np.compress(s <= eps, vh, axis=0)
        print("\nnullspace:\n",null_space)
        print("\noriginal matrix:\n",(u * s) @ vh)
        for i in range(len(self.states)):
            s = ""
            for j in range(len(self.states)):
                s =s+ str(self.q[i][j])+" "
            print(s)
