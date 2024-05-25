import sys
from collections import deque

input = sys.stdin.readline

# 가로 세로 입력
m, n = map(int, input().split())

# 입력값에 따른 필드 초기화
field = [list(map(str, input().rstrip())) for _ in range(n)]

# 방문 여부 확인
chk = [[False] * m for _ in range(n)]

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x, army) :
    q = deque([(y, x)])

    # 인접한 군대 수 카운트
    near_army = 1

    while q :
        y, x = q.popleft()
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            # 필드 범위 벗어 나는 경우
            if (ny < 0 or ny >= n) or (nx < 0 or nx >= m) :
                continue
            # 찾고자 하는 부대 이외의 경우
            if field[ny][nx] != army :
                continue

            # 부대가 연결되어 있는 경우 카운트
            if field[ny][nx] == army and not(chk[ny][nx]) :
                chk[ny][nx] = True
                near_army += 1
                q.append((ny, nx))
    
    # 인접된 군대 수의 제곱을 저장
    return near_army ** 2

result = []

# B군대 탐색
for j in range(n) :
    for i in range(m) :
        if not(chk[j][i]) and field[j][i] == 'B' :
            chk[j][i] = True
            result.append(bfs(j, i, 'B'))

# B군대 합
B_sum = sum(result)

result.clear()

# W군대 탐색
for j in range(n) :
    for i in range(m) :
        if not(chk[j][i]) and field[j][i] == 'W' :
            chk[j][i] = True
            result.append(bfs(j, i, 'W'))

# W군대 합
W_sum = sum(result)

print(W_sum, B_sum)