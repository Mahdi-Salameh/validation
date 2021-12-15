# -*- coding: utf-8 -*-
"""
Created Tuesday November 30 21:36:20 2021

@author: ALBasha_OJEIMI_SALAMEH
"""


from typing import Deque


def find_accepting_bfs(graph):
    known = dict()  # Known
    frontier = Deque()  # Frontier #list_des_noeuds
    at_start = True  # init

    while frontier or at_start:
        if at_start:
            neighbours = graph.initial()
            at_start = False
        else:
            neighbours = graph.next(frontier.popleft())
        for n in neighbours:

            if n not in known:
                if graph.is_accepting(n):
                    return True, n
                known[n] = n
                frontier.append(n)

    return False, None


def predicate_model_checker(function, value):
    return True
