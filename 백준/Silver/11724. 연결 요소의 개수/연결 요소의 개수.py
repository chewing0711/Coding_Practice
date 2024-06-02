"""
아이디어 :
 - 방문여부 for문으로 시작노드 결정, False -> 시작노드 True->다음
 - dfs or bfs로 시작노드를 중심으로 visited를 트루로 바꿈 dfs한번 할 때마다 cnt += 1
 - bfs로 푸는게 바람직해보이지만, dfs연습을 위해서 dfs로 작성

시간복잡도 : dfs시간복잡도 O(n+v)이므로 O(1000+1000*500) = O(50만), dfs를 n번돌아야함

자료구조 : bool[] 방문여부 , graph int[][]

"""


import sys

# Recursion limit 설정
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())

able = [[0] * n for _ in range(n)]

visited = [False] * n

for _ in range(m) :
    node1, node2 = map(int, input().split())

    node1 -= 1
    node2 -= 1

    able[node1][node2] = 1
    able[node2][node1] = 1

def dfs(node) :
    visited[node] = True

    for i in range(n) :
        if able[node][i] == 1 and not(visited[i]) :
            dfs(i)

count = 0

for i in range(n) :
    if not(visited[i]) :
        count += 1
        dfs(i)

print(count)