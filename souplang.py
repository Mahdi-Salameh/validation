from kernel import *
import copy


class Behavior_Soup:
    def __init__(self, conf):
        self.initial = conf
        self.behaviors = []

    def add(self, n, g, a):
        self.behaviors.append(Behavior(n, g, a))


class Behavior:
    def __init__(self, name, g, a):
        self.name = name
        self.action = a
        self.guard = g
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

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
