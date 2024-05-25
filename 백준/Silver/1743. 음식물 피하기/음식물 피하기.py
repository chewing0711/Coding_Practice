import sys
from collections import deque

input = sys.stdin.readline

# 세로 가로 영역좌표
n, m, k = map(int, input().split())

# 필드 초기화
field = [[0] * m for _ in range(n)]

# 방문 여부 확인
chk = [[False] * m for _ in range(n)]

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 입력값에 따른 필드에 영역 생성
for _ in range(k) :
    y, x = map(int, input().split())
    field[y - 1][x - 1] = 1

def bfs(y, x) :
    q = deque([(y, x)])

    # 찾고자 하는 영역의 크기
    size = 1

    # 탐색
    while q :
        y, x = q.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if (ny < 0 or ny >= n) or (nx < 0 or nx >= m) :
                continue

            if field[ny][nx] == 0 :
                continue

            if not(chk[ny][nx]) :
                chk[ny][nx] = True
                q.append((ny, nx))
                size += 1

    return size


# 영역 값을 저장
result = []

# 2중 반복문으로 필드 탐색
for j in range(n) :
    for i in range(m) :
        if not(chk[j][i]) and field[j][i] == 1 :
            chk[j][i] = True
            result.append(bfs(j, i))

print(max(result))