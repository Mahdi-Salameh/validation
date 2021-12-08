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
