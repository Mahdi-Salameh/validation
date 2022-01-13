# -*- coding: utf-8 -*-
"""
Created Tuesday November 24 14:19:20 2021

@author: ALBasha_OJEIMI_SALAMEH
"""
# test commit git ghfhg
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
# -----------------<Importing the necessary library>-----------------
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

from itertools import count
import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import nodes
from networkx.generators.classic import null_graph
from algorithms import *
from simpleGraph import *
from counter import *
from souplang import *
from Predicate import *
from aliceBobV0 import *
from hanoi import *
from counter import *

def main_networkx():

    G = nx.DiGraph()

    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    # ------------------------<Adding the nodes>-------------------------
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    # Add node S having a position on the graph page as x = 13 and y = 3
    G.add_node("S", pos=(13, 3))
    # Add node A having a position on the graph page as x = 14.5 and y = 6
    G.add_node("A", pos=(14.5, 6))
    # Add node B having a position on the graph page as x = 14.5 and y = 0
    G.add_node("B", pos=(14.5, 0))
    # Add node C having a position on the graph page as x = 18 and y = 4
    G.add_node("C", pos=(16, 6))
    # Add node C having a position on the graph page as x = 18 and y = 4
    G.add_node("D", pos=(16, 0))
    # Add node C having a position on the graph page as x = 18 and y = 4
    G.add_node("T", pos=(18, 3))
    # Add node X having a position on the graph page as x = 19 and y = 4
    G.add_node("X", pos=(19, 4))

    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    # -------<Adding the edges connected to nodes with the weight>-------
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    # Add edge from S to A having a weight equal to 16
    G.add_edge("S", "A", weight=16)
    # Add edge from S to B having a weight equal to 13
    G.add_edge("S", "B", weight=13)
    # Add edge from A to C having a weight equal to 12
    G.add_edge("A", "C", weight=12)
    # Add edge from A to B having a weight equal to 4
    G.add_edge("A", "B", weight=4)
    # Add edge from C to T having a weight equal to 20
    G.add_edge("C", "T", weight=20)
    # Add edge from B to D having a weight equal to 14
    G.add_edge("B", "D", weight=14)
    # Add edge from B to C having a weight equal to 9
    G.add_edge("C", "B", weight=9)
    # G.add_edge("B", "A", weight=10)#Add edge from B to A having a weight equal to 10
    # Add edge from D to T having a weight equal to 4
    G.add_edge("D", "T", weight=4)
    # Add edge from D to C having a weight equal to 7
    G.add_edge("D", "C", weight=7)

    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    # -----------------<Adding the weights on the edges>----------------
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    pos = nx.get_node_attributes(G, 'pos')
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    nx.draw(G, pos, with_labels=True)

    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    # ----------------<Defining the source and the target>---------------
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    Source = "S"
    Target = "T"

    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    # --------<Printing the shortest path from source to target>---------
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    shortest_path = nx.shortest_path(G, source=Source, target=Target)
    # print(shortest_path)

    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    # -----------------<Function to iterate the Graph>-------------------
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    def iterate():
        L = list(G.nodes)
        for i in range(len(L)):
            if len(list(G.neighbors(L[i]))) == 0:
                print("The node", L[i], "has no neighbors")
            else:
                print("The node", L[i], "has the following neighbors :")
                print([n for n in G.neighbors(L[i])])

    iterate()
    g = NFA(G, ['A'], ['B', 'T'])
    # temp, n = find_accepting_bfs(g)
    # if temp:
    #     print(n)
    known = find_accepting_bfs(g)
    print("Accessible nodes from A: ", known)
    plt.show()

    #semantics = BehSoupSemantics(counter(3))
    # predicate_model_checker(semantics, lambda c: c.pc == 2)
    # predicate_model_checker(semantics, lambda c: c.pc > 50)

def main_hanoi_1():
    # Input: number of disks
    num_of_disks = 4

    # Create three stacks of size 'num_of_disks'
    # to hold the disks
    src = createStack(num_of_disks)
    dest = createStack(num_of_disks)
    aux = createStack(num_of_disks)

    tohIterative(num_of_disks, src, aux, dest)

def main_hanoi_2():
    print("-------------------------")
    print("Guarde / Action")
    print("Example 1: ")
    hanoi_tower = ParentStore_Proxy(Hanoi(3,3))
    for i, j in [(0, 1), (0, 2), (2, 1)]:
        init = hanoi_tower.initial()[0]
        guarde = guarde_def(i, j)
        action = action_def(i, j)
        g = guarde(init)
        if g:
            a = action(init)
        print(f'{i},{j} : {"Vrai" if g else "Faux"} -> {init}')

    print("Example 2: ")
    init = hanoi_tower.initial()[0]
    for i, j in [(0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2)]:
        guard = guarde_def(i, j)
        action = action_def(i, j)
        g = guard(init)
        if g:
            a = action(init)
        print(f'{i},{j} : {"Vrai" if g else "Faux"} -> {init}')

    print("-------------------------")
    print("Soup")
    soup = hanoi_soap(3, 3)
    Behavior_Soup = BehSoupSemantics(soup)
    init = Behavior_Soup.initial()[0]
    print("First State: ", init)
    actions = Behavior_Soup.actions(init)

    if actions:
        print("Possible action : ", inspect.getsource(action))
        for action in actions:
            execute = Behavior_Soup.execute(init, action)
            print("Execution output : ", execute)

    print("-------------------------")

    print("STR2TR")
    str = STR2TR(Behavior_Soup)
    init = str.initial()[0]
    next = str.next(init)
    print("States after ", init, "are", next)

    print("-------------------------")


def main_counter():
    semantics = BehSoupSemantics(counter(5))
    print(semantics.initial())
    print(semantics.actions(semantics.initial()[0]))
    r = bfs(STR2TR(semantics))
    print(r)
    predicate_model_checker(semantics, lambda c: c.jpc == 2)
    # print(r)
    predicate_model_checker(semantics, lambda c: c.jpc > 50)
    # print(r)

def main_alice_bob():
    semantics = BehSoupSemantics(aliceBob())
    # print(semantics.initial())
    # print(semantics.actions(semantics.initial()[0]))

    # for action in semantics.actions(semantics.initial()[0]):
    #     print(inspect.getsource(action))

    # print(inspect.getsource(semantics.actions(semantics.initial()[0]) ))

    r = bfs(STR2TR(semantics))
    print("States: ", r) 

    predicate_model_checker(semantics, lambda c: c.bpc == 0)

    print("Deadlock Test: ", end=" ")
    predicate_model_checker(semantics, lambda c: len(semantics.actions(c)) == 0 )
    print("Critical section Test: ", end=" ")
    predicate_model_checker(semantics, lambda c: c.apc == 1 and c.bpc == 1 )


if __name__ == "__main__":
    print("1: Graph")
    print("2: Hanoi V1")
    print("3: Hanoi V2")
    print("4: Counter")
    print("5: AliceBob")
    option = input("What is your choice? ")

    if option == '1':
        main_networkx()
    elif option == '2':
        main_hanoi_1()
    elif option == '3':
        main_hanoi_2()
    elif option == '4':
        main_counter()
    elif option == '5':
        main_alice_bob()
