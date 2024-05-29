import sys
from collections import deque

input = sys.stdin.readline

node, line, start = map(int, input().split())

field = [[0] * node for _ in range(node)]

for _ in range(line) :
    node1, node2 = map(lambda x: int(x) - 1, input().split())
    field[node1][node2] = 1
    field[node2][node1] = 1

visited_bfs = [False] * node
visited_dfs = [False] * node

bfs_result = []
dfs_result = []


def bfs(n) :
    q = deque([n])
    visited_bfs[n] = True
    bfs_result.append(n + 1)
    while q :
        N = q.popleft()
        for i in range(node) :
            if not(visited_bfs[i]) and field[N][i] == 1 :
                visited_bfs[i] = True
                bfs_result.append(i + 1)
                q.append(i)


def dfs(n) :
    visited_dfs[n] = True
    dfs_result.append(n + 1)

    for i in range(node) :
        if not(visited_dfs[i]) and (field[n][i] == 1) :
            dfs(i)


bfs(start - 1)
dfs(start - 1)


for i in dfs_result :
    print(i, end = ' ')

print()

for i in bfs_result :
    print(i, end = ' ')