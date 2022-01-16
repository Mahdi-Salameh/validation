class Transition_Relation:
    def initial(self): pass
    def next(self, c): pass


class AcceptingSet:
    def is_accepting(c): pass


class Identity_Proxy:
    def __init__(self, operand):
        self.operand = operand

    def __getattr__(self, attr):
        return getattr(self.operand, attr)


class ParentStore_Proxy (Identity_Proxy):

    def __init__(self, op):
        super().__init__(op)
        self.parent = {}

    def next(self, conf):
        nS = self.operand.next(conf)

        for n in nS:
            if n not in self.parent:
                self.parent[n] = conf

        return nS

class SemanticTransitionRelation: 
    def initial (self):pass
    def actions (self, conf): pass
    def execute (self, conf, action):pass


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

class STR2oSTR:
    def __init__(self,operand):
        self.operand = operand

    def initial(self):
        return self.operand.initial()

    def actions(self, c):
        return self.operand.actions(c)

    def execute(self, c, source, a):
        target = self.operand.execute(c,a)
        return (source, a, target), target

class iSTR:
    def __init__(self, str):
        self.operand = str
    
    def actions(self, i, conf):
        actions = self.operand.actions(conf)
        for a in actions:
            if a[0](i):
                actions.append(a)
        return actions
    
    def execute(self, i, conf, actions):
        targets =[]
        for a in actions(conf):
            target = self.operand.execute(conf,a)
            target.append(target)
        return targets[conf](i)

class oSTR:
    def __init__(self, str):
        self.operand = str
    
    def actions(self, conf):
        return self.operand.actions(conf)

    def execute(self, conf, actions):
        targets = []
        for a in actions(conf):
            target = self.operand.execute(conf, a)
            targets.append(target)
        return targets, self.operand

class KripkeBuchiSTR(SemanticTransitionRelation):

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def initial(self):
        return list(map(lambda rc: (None, rc), self.rhs.initial()))

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
                num_actions -= 1
            self.get_synchronons_actions(k_target,buchi_src,synchronons_actions)
            
            if num_actions == 0:
                self.get_synchronons_actions(kripke_src,buchi_src,synchronons_actions)

    def get_synchronons_actions(self,kc,bc,io_synca):
        buchi_actions = self.rhs.actions(kc,bc)
        return io_synca.extend(map(lambda ba:(kc,ba),buchi_actions))

    def execute(self,action,conf):
        ktarget,baction = action
        _,bsrc = conf
        return ktarget,self.rhs.execute(ktarget,baction,bsrc)

class buchiSemantics(iSTR):
    def __init__(self, t):
        self.initial = t[0]
        self.delta = t[1]
        self.predi = t[2]

    def initial(self):
        return [self.initial]

    def actions(self, i, c):
        actions = []
        for a in self.delta[c]:
            if a[0](i):
                actions.append(a)
        return actions

    def execute(self, i, conf, a):
        return a[1]
    
