from souplang import *
from algorithms import *
from kernel import *
import inspect

class aliceBobConfig:
    def __init__(self):
        self.alice_pc = 0
        self.bob_pc = 0
        self.alice_flag = 0
        self.bob_flag = 0

    def __hash__(self):
        return hash(self.alice_pc + self.bob_pc) + hash(self.alice_flag + self.bob_flag)

    def __eq__(self, other):
        if other is None:
            return False
        return self.alice_pc == other.alice_pc and self.bob_pc == other.bob_pc and self.bob_flag == other.bob_flag and self.alice_flag == other.alice_flag

    def __repr__(self):
        return str(self.alice_pc) + str(self.bob_pc)


def aliceBob():
    soup = Behavior_Soup(aliceBobConfig())

    def InitialToWait_alice(c):
        c.alice_pc = 1
        c.alice_flag = 1

    soup.add("InitialToWait_alice", lambda c: c.alice_pc == 0, InitialToWait_alice)

    def WaitToCriticalSec_Alice(c):
        c.alice_pc = 2
        c.alice_flag = 1

    soup.add("WaitToCriticalSec_Alice", lambda c: c.bob_pc != 2 and c.alice_pc == 1, WaitToCriticalSec_Alice)

    def CriticalSectionToInitial_Alice(c):
        c.alice_pc = 0
        c.alice_flag = 0

    soup.add("CriticalSectionToInitial_Alice", lambda c: c.alice_pc == 2, CriticalSectionToInitial_Alice)

    def InitialToWait_bob(c):
        c.bob_pc = 1
        c.bob_flag = 1

    soup.add("InitialToWait_bob", lambda c: c.bob_pc == 0, InitialToWait_bob)

    def WaitToCriticalSec_Bob(c):
        c.bob_pc = 2
        c.bob_flag = 1

    soup.add("WaitToCriticalSec_Bob", lambda c: c.bob_pc == 1 and c.alice_pc != 2, WaitToCriticalSec_Bob)

    def CriticalSectionToInitial_Bob(c):
        c.bob_pc = 0
        c.bob_flag = 0

    soup.add("CriticalSectionToInitial_Bob", lambda c: c.bob_pc == 2, CriticalSectionToInitial_Bob)

    return soup


def alice_InCS(c):
    return c.alice_pc == 2


def bob_InCS(c):
    return c.bob_pc == 2


def exclusion_buchi():
    delta = {0: [(lambda c: True, 0), (lambda c: alice_InCS(c) and bob_InCS(c), 1)], 1: [(lambda c: True, 1)]}
    return 0, delta, lambda c: c == 1


if __name__ == '__main__':
    semantics = BehSoupSemantics(aliceBob())
    # r = predicate_model_checker(semantic, lambda c: c.alice_pc == 2 and c.bob_pc == 2)
    # print(r)
    # r = predicate_model_checker(semantic, lambda c: len(semantic.actions(c)) == 0)
    # print(r)
    bushi = buchiSemantics(exclusion_buchi())
    Sync = KripkeBuchiSTR(semantics,bushi)
    tr = predicate_model_checker(Sync,lambda c:  bushi.pred(c[1]))
    print(tr)
    tr = model_checker(semantics, bushi)
    print(tr)