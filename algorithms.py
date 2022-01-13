# -*- coding: utf-8 -*-
"""
Created Tuesday November 30 21:36:20 2021

@author: ALBasha_OJEIMI_SALAMEH
"""


from typing import Deque

from STR2TR import STR2TR, isAcceptingProxy
from kernel import ParentStore_Proxy


def bfs(graph):
    known = set()  # Known
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
                known.add(n)
                frontier.append(n)

    return known

def find_accepting_bfs(graph):
    known = set()  # Known
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
                known.add(n)
                frontier.append(n)

    return known

def is_bfs_reachable(graph, start, end):
    known = set()  # Known
    frontier = Deque()  # Frontier #list_des_noeuds
    neighbours = [start]
    for i in neighbours:
        if i not in known:
            known.add(i)
            frontier.append(i)
    while frontier:
        neighbours = graph.next(frontier.popleft())
        for i in neighbours:
            if i == end:
                return True
            if i not in known:
                known.add(i)
                frontier.append(i)
    return False


def is_bfs_safe(graph):
    known = set()  # Known
    frontier = Deque()  # Frontier #list_des_noeuds
    at_start = True  # init

    while frontier or at_start:
        if at_start:
            neighbours = [graph.initial()]
            at_start = False
        else:
            neighbours = graph.next(frontier.popleft())
        for n in neighbours:
            
            if n not in known:
                if graph.is_accepting(n):
                    return False
                known[n] = n
                frontier.append(n)

    return True

def find_acceptingbfs(g, initial = None):
    known = set()
    frontier = Deque()
    at_start = True
    while frontier or at_start:
        if at_start:
            if initial:
                neighbours = initial
            else:
                neighbours = g.initial()
            at_start = False
        else:
            neighbours = g.next(frontier.popleft())
        for n in neighbours:
            if g.is_accepting(n):
                return True, n
            if n not in known:
                known.add(n)
                frontier.append(n)
    return False, None



def predicate_model_checker(semantics, predicate):
    tr = STR2TR(semantics)

    tr = isAcceptingProxy(tr, predicate)

    tr = ParentStore_Proxy(tr)
    r = find_accepting_bfs(tr)


def get_trace(parents, result, initial):
    status,target = result
    if not status :
        print("Accepting State Not found!")
        return None
    print (initial,result)

    currentNode = target
    trace = [currentNode]
    while currentNode not in initial:
        currentNode = parents[currentNode]
        trace.append(currentNode)

    print("Trace : ", trace)
