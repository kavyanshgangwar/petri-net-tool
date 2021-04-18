from Place import Place
from Arc import Arc
from Transition import Transition
import numpy as np
from Petrinet import Petrinet

class Complete(Petrinet):
    def __init__(self):
        super().__init__()


    def get_index(self,marking):
        for i in range(len(self.states)):
            if marking == self.states[i]:
                return i
        return -1

    def get_subset_prob(self,markings):
        size = len(self.PIE)
        res = np.zeros((size))
        for i in range(size):
            for marking in markings:
                res[i] += self.PIE[i][self.get_index(marking)]
        return res

    def get_max_at_place_i(self,place_index):
        nax = 0
        for state in self.states:
            nax = max(nax,state[place_index])
        return nax

    def get_mean_tokens_place(self,place_i):
        place_index = self.placeindex[place_i]
        size = len(self.PIE)
        res = np.zeros((size))
        nax = self.get_max_at_place_i(place_index)
        for token_no in range(1,nax+1):
            markings = []
            for state in self.states:
                if state[place_index] == token_no:
                    markings.append(state)
            res = np.add(res,token_no * self.get_subset_prob(markings))
        return res

    def find_transition_subset(self,trans):
        markings = []
        for state in self.states:
            if trans.can_fire(state,self.placeindex):
                markings.append(state)
        return markings

    def probability_firing_trans(self,trans):
        size = len(self.PIE)
        res = np.zeros((size))
        markings = self.find_transition_subset(trans)
        for marking in markings:
            mark_index = self.get_index(marking)
            temp = self.get_subset_prob([marking])
            temp = temp / (-self.Q[mark_index][mark_index])
            res = np.add(res,temp)
        res = res * trans.lambdai
        return res

    def  Throughtput(self,trans):
        size = len(self.PIE)
        res = np.zeros((size))
        markings = self.find_transition_subset(trans)
        # print("markings are:",markings)
        # print(trans.lambdai)
        res = self.get_subset_prob(markings)
        # print("res from previous is:",res)
        res = res*trans.lambdai
        return res
