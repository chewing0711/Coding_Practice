import sys
from collections import deque

input = sys.stdin.readline

# 필드 크기 입력
n, m = map(int, input().split())

field = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

chk = [[False] * m for _ in range(n)]

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x) :
    queue = deque([(y, x)])
    chk[y][x] = True
    while queue:

        y, x = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 > nx or nx >= m) or (0 > ny or ny >= n) :
                continue
            if field[ny][nx] == 0 :
                continue
            if not(chk[ny][nx]) :
                chk[ny][nx] = True
                field[ny][nx] = field[y][x] + 1
                queue.append((ny, nx))

    return field[n - 1][m - 1]

print(bfs(0, 0))