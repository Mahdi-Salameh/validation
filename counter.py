from BehaviorSoup import *
from souplang import *
from algorithms import *
from STR2TR import *
from kernel import *


class CounterConfig:
    def __init__(self):
        self.jpc = 0

    def __hash__(self):
        return int(hash(self.jpc))

    def __eq__(self, other):
        return self.jpc == other.jpc

    def __repr__(self):
        return str(self.jpc)


def counter(max):
    instanceConfCount = CounterConfig()
    soup = Behavior_Soup(instanceConfCount)

    def inc(c):
        c.jpc = c.jpc + 1

    soup.add("t", lambda c: c.jpc < max, inc)

    def reset(c):
        c.jpc = 0

    soup.add("r", lambda c: c.jpc >= max, reset)

    return soup


if __name__ == "__main__":
    semantics = BehSoupSemantics(counter(5))
    #print(semantics.initial())
    #print(semantics.actions(semantics.initial()[0]))
    r = bfs(STR2TR(semantics))
    #print(r)
    predicate_model_checker(semantics, lambda c: c.jpc == 2)
    #print(r)
    #predicate_model_checker(semantics, lambda c: c.jpc > 50)
    #print(r)