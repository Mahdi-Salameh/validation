from BehaviorSoup import *


class CounterConfig:
    def __init__(self):
        self.pc = 0

    def __hash__(self):
        return hash(self.pc)

    def __equals__(self, other):
        return self.pc == other .pc


def counter(max):
    soup = Behavior_Soup((CounterConfig))

    def inc(c):
        c.pc = c.pc + 1

    soup.add("t", lambda c: c.pc < max, inc)

    def reset(c):
        c.pc = 0

    soup.add("r", lambda c: c.pc >= max, reset)

    return soup
