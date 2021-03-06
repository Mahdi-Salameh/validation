from kernel import *

class SimpleGraph(Transition_Relation):

    def __init__(self, g, iniS):
        self.g = g
        self.iniS = iniS


    def initial(self):
        return self.iniS

    def next(self, c):
        try:
            return self.g.successors(c)
        except:
            return []

class NFA(SimpleGraph, AcceptingSet):

    def __init__(self, g, iniS, acc):
        super().__init__(g, iniS)
        self.accepting = acc

    def is_accepting(self, c):
        return c in self.accepting


    

