# -*- coding: utf-8 -*-
"""
Created Tuesday November 24 14:19:20 2021

@author: ALBasha_OJEIMI_SALAMEH
"""
#test commit git ghfhg
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
# -----------------<Importing the necessary library>-----------------
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

from itertools import count
import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import nodes
from networkx.generators.classic import null_graph
from algorithms import *

if __name__ == "__main__":

    G = nx.DiGraph()

    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    # ------------------------<Adding the nodes>-------------------------
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    G.add_node("S",pos=(13,3)) #Add node S having a position on the graph page as x = 13 and y = 3
    G.add_node("A",pos=(14.5,6))#Add node A having a position on the graph page as x = 14.5 and y = 6
    G.add_node("B",pos=(14.5,0))#Add node B having a position on the graph page as x = 14.5 and y = 0
    G.add_node("C",pos=(16,6))#Add node C having a position on the graph page as x = 18 and y = 4
    G.add_node("D",pos=(16,0))#Add node C having a position on the graph page as x = 18 and y = 4
    G.add_node("T",pos=(18,3))#Add node C having a position on the graph page as x = 18 and y = 4
    G.add_node("X",pos=(19,4))#Add node X having a position on the graph page as x = 19 and y = 4


    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    # -------<Adding the edges connected to nodes with the weight>-------
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    G.add_edge("S", "A", weight=16)#Add edge from S to A having a weight equal to 16
    G.add_edge("S", "B", weight=13)#Add edge from S to B having a weight equal to 13
    G.add_edge("A", "C", weight=12)#Add edge from A to C having a weight equal to 12
    G.add_edge("A", "B", weight=4)#Add edge from A to B having a weight equal to 4    
    G.add_edge("C", "T", weight=20)#Add edge from C to T having a weight equal to 20
    G.add_edge("B", "D", weight=14)#Add edge from B to D having a weight equal to 14
    G.add_edge("C", "B", weight=9)#Add edge from B to C having a weight equal to 9
    #G.add_edge("B", "A", weight=10)#Add edge from B to A having a weight equal to 10    
    G.add_edge("D", "T", weight=4)#Add edge from D to T having a weight equal to 4
    G.add_edge("D", "C", weight=7)#Add edge from D to C having a weight equal to 7


    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    # -----------------<Adding the weights on the edges>----------------
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    pos = nx.get_node_attributes(G,'pos')
    labels = nx.get_edge_attributes(G,'weight')

    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    nx.draw(G, pos, with_labels=True)

    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    # ----------------<Defining the source and the target>---------------
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    Source = "S"
    Target = "T"

    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    # --------<Printing the shortest path from source to target>---------
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    shortest_path = nx.shortest_path(G,source=Source,target=Target)
    #print(shortest_path)

    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    # -----------------<Function to iterate the Graph>-------------------
    # -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    
    def iterate():
        L = list(G.nodes)
        for i in range(len(L)):
            if len(list(G.neighbors(L[i]))) == 0:
                print("The node",L[i], "has no neighbors")
            else:
                print("The node",L[i], "has the following neighbors :")
                print([n for n in G.neighbors(L[i])])
        

    # iterate()
    is_safe_bfs(G, ['X','A'])
    plt.show()
