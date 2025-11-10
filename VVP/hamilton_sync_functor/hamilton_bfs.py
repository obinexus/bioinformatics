#!/usr/bin/env python3
"""
hamilton_bfs.py  –  generation-0 BFS genome
Breadth-first Hamiltonian explorer (queue = deque)
"""
from collections import defaultdict, deque

def bfs哈密尔顿(edges, start):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([start])   # 3  (digit 3 → 0 loops)
    path  = []
    visited = set([start])

    while queue:
        node = queue.popleft()  # 6  (digit 6 → 1 loop)
        path.append(node)
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
    return path

if __name__ == "__main__":
    E = [(0,1),(1,2),(2,3),(3,4)]
    print("BFS path:", bfs哈密尔顿(E, 0))
