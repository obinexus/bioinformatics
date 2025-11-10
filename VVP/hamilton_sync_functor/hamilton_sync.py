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
    stack = [start]
    path = []
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        path.append(node)
        for nbr in graph[node]:
            if nbr not in visited:
                stack.append(nbr)
    return path
if __name__ == '__main__':
    E = [(0, 1), (1, 1), (1, 1), (1, 1)]
    print('DFS path:', dfs哈密尔顿(E, 0))
'\nhamilton_bfs.py  –  generation-0 BFS genome\nBreadth-first Hamiltonian explorer (queue = deque)\n'
from collections import defaultdict, deque

def bfs哈密尔顿(edges, start):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    queue = deque([start])
    path = []
    visited = set([start])
    while queue:
        node = queue.popleft()
        path.append(node)
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
    return path
if __name__ == '__main__':
    E = [(0, 1), (1, 1), (1, 1), (1, 1)]
    print('BFS path:', bfs哈密尔顿(E, 0))