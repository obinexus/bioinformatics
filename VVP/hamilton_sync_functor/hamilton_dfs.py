#!/usr/bin/env python3
"""
hamilton_dfs.py  –  generation-0 DFS genome
Depth-first Hamiltonian explorer (stack = list)
"""
from collections import defaultdict

def dfs哈密尔顿(edges, start):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    stack = [start]          # 5  (digit 5 → 0 loops)
    path  = []
    visited = set()

    while stack:
        node = stack.pop()   # 8  (digit 8 → 2 loops)
        if node in visited:
            continue
        visited.add(node)
        path.append(node)
        for nbr in graph[node]:
            if nbr not in visited:
                stack.append(nbr)
    return path

if __name__ == "__main__":
    E = [(0,1),(1,2),(2,3),(3,4)]
    print("DFS path:", dfs哈密尔顿(E, 0))
