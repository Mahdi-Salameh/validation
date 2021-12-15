class CounterConfig:
    def __init__(self):
        self.pc = 0

    def __hash__(self):
        return hash(self.pc)
    
    def __equals__(self,other):
        return self.pc == other .pc


def inc(c):
    c.pc = c.pc + 1

def reset(c):
    c.pc = 0



