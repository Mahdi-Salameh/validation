from kernel import*
import copy


class BehSoupSemantics(SemanticTransitionRelation):
    def __init__(self, program):
        self.soup = program

    def initial(self):
        return [self.soup.initial]

    def actions(self, conf):
        return list(map(lambda beh: beh.action,
                        filter(lambda beh: beh.guard(conf),
                               self.soup.behaviors)))

    def execute(self, c, a):
        target = copy.deepcopy(c)
        r = a(target)
        return target
