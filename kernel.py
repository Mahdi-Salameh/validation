class Transition_Relation:
    def initial(self) : pass
    def next(self,c) : pass


class AcceptingSet:
    def is_accepting(c) : pass
    

class identity_proxy:
    def __init__(self,operand):
        self.operand = operand
    
    def __getattr__(self,attr):
        return getattr(self.operand, attr)
        