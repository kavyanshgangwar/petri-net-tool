from copy import deepcopy
class Tokenslist():
    """docstring for Tokenslist."""

    def __init__(self,lst):
        self.lst = deepcopy(lst)
    def hasatleast(self,place,nin):
        if self.lst[place] >= nin:
            return True
        return False
    def set_lst(self,lst):
        self.lst = deepcopy(lst)
    def get_lst(self):
        return deepcopy(self.lst)
    def alter_tokens_at_place(self,place,amount):
        self.lst[place] += amount
