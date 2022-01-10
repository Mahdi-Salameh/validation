from kernel import *

class STR2oSTR:
    def __init__(self,operand):
        self.operand = operand

    def initial(self):
        return self.operand.initial()

    # def actions(self,c):
    #     return self.operand.actions(c)

    # def execute(self,source,a):
    #     target = self.operand.execute(c,a)
    #     return (source,a,target),target

    def actions(self,source):
        synchronons_actions = []
        kripke_src, buchi_src = source
        if kripke_src in None:
            for k_target in self.lhs.initial():
                self.get_synchronons_actions(k_target,buchi_src,synchronons_actions)
            return synchronons_actions
        k_actions = self.lhs.actions(kripke_src)
        num_actions = len(k_actions)
        for ka in k_actions:
            _,k_target = self.lhs.execute(kripke_src,ka)
            if k_target is None:
                num_action -= 1
                self.get_synchronons_actions(k_target,buchi_src,synchronons_actions)
            if num_actions == 0:
                self.get_synchronons_actions(kripke_src,buchi_src,synchronons_actions) 