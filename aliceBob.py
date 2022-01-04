from BehaviorSoup import *
from souplang import *
from algorithms import *
from STR2TR import *
from kernel import *


class aliceBobConfig:
    def __init__(self):
        self.apc = 0
        self.bpc = 0

    def __hash__(self):
        return int(hash(self.apc + self.bpc)) 

    def __eq__(self, other):
        return self.apc == other.apc & self.bpc == other.bpc

    def __repr__(self):
        return str(self.apc) + str(self.bpc)


def aliceBob(maxi):
    instanceConfCount = aliceBobConfig()
    soup = Behavior_Soup(instanceConfCount)

    def aliceBobToInit(c):
        c.apc = 0
        c.bpc = 0

    soup.add("aliceBobToInit", lambda c: c.apc < maxi, aliceBobToInit)

    def aToSc(c):
        c.apc = 1
        c.bpc = 0

    soup.add("aToSc", lambda c: c.apc < maxi, aToSc)

    def bToSc(c):
        c.apc = 0
        c.bpc = 1

    soup.add("bToSc", lambda c: c.bpc < maxi, bToSc)


    def aliceBobToSc(c):
        c.apc = 1
        c.bpc = 1

    soup.add("aliceBobToSc", lambda c: c.apc + c.bpc == maxi, aliceBobToSc)

    return soup


if __name__ == "__main__":
    semantics = BehSoupSemantics(aliceBob(2))
    print(semantics.initial())
    print(semantics.actions(semantics.initial()[0]))

    # r = bfs(STR2TR(semantics))
    # print(r)

    predicate_model_checker(semantics, lambda c: c.apc == 0)
