from kernel import*


class BehSoupSemantics(SemanticTransitionRelation):
    def __init__(self, program):
        self.soup = program

    def initial(self):
        return [self.soup.initial]

    def actions(self, conf):
        return list(map(lambda beh: beh.action,
                        filter(lambda beh: beh.guard(conf),
                               self.soup.behaviours)))

    def execute(self, c, a):
        target = self.copy.deepcopy(c)
        r = a(target)
        return target