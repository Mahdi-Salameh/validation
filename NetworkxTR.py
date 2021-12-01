# -*- coding: utf-8 -*-
"""
Created Tuesday November 30 21:36:20 2021

@author: ALBasha_OJEIMI_SALAMEH
"""

def is_safe_bfs(g, start):
        K = [] #Known
        F = [] #Frontier #list_des_noeuds
        i = True #init

        while len(F)>0 or i:
            if i:
                N = start
                i = False
            else:
                N = g.successors( F.pop(0) )
            for n in N:
                if n not in K:
                    K.append(n)
                    F.append(n)
            
        print(K)

class NetworkxTR:
    
    def _init_(self, g):
        self.__g = g
