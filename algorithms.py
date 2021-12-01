# -*- coding: utf-8 -*-
"""
Created Tuesday November 30 21:36:20 2021

@author: ALBasha_OJEIMI_SALAMEH
"""


def find_accepting_bfs(graph):
    known = []  # Known
    frontier = []  # Frontier #list_des_noeuds
    at_start = True  # init

    while frontier or at_start:
        if at_start:
            neighbours = graph.initial()
            at_start = False
        else:
            neighbours = graph.next(frontier.pop(0))
        for n in neighbours:
            if graph.is_accepting(n):
                return True, n

            if n not in known:
                known.append(n)
                frontier.append(n)

    return False, None
