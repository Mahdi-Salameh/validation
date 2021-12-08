from kernel import *


class STR2TR:
    def __init__(self, str):
        self.operand = str

    def initial(self):
        return self.operand.initial()

    def next(self, c):
        targets = []
        for a in self.operand.actions(c):
            target = self.operand.execute(c, a)
            targets.append(target)
        return targets


class isAcceptingProxy(Identity_Proxy):
    def __init__(self, operand, predicate):
        super().__init__(operand)
        self.predicate = predicate

    def is_accepting(self, c):
        return self.predicate(c)
