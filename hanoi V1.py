import copy
from kernel import *
from souplang import *
#from algorithms import find_acceptingbfs


class HConfig(list):
    
    def __init__(self, Stacks_Numb, Disks_Numb):
        list.__init__(self, [[(Disks_Numb - i) for i in range(Disks_Numb)]] + [[] for _ in range(Stacks_Numb - 1)])

    def __hash__(self):
        maximum = max(self)[0]
        hash = 0
        for nbStacks in self:
            hash += sum(nbStacks) * maximum
            maximum *= 2
        return hash

    def __eq__(self, configuration):
        if len(self) != len(configuration):
            return False
        for j in range(len(self)):
            if len(self[j]) != len(configuration[j]):
                return False
            for i in range(len(self[j])):
                if configuration[j][i] != self[j][i]:
                    return False
        return True


class HanoiTower(Transition_Relation, AcceptingSet):

    def __init__(self, Stacks_Numb, Disks_Numb):
        self.nbDisks = Disks_Numb
        self.nbStacks = Stacks_Numb

    def initial(self):
        return [HConfig(self.nbStacks, self.nbDisks)]

    def next(self, Nodes):
        NextEtat = []
        for x in range(self.nbStacks):
            new_Node = copy.deepcopy(Nodes)
            if new_Node[x]:
                disque = new_Node[x].pop()
                for i in range(self.nbStacks):
                    if x != i and (not new_Node[i] or new_Node[i][-1] > disque):
                        temporary = copy.deepcopy(new_Node)
                        temporary[i].append(disque)
                        NextEtat.append(temporary)
        return NextEtat

    def is_accepting(self, c):
        k = 0
        if not c[-1]:
            return False
        for disk in c[-1]:
            if disk != self.nbDisks - k:
                return False
            k += 1
        return True

