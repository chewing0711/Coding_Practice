import sys
from collections import deque

input = sys.stdin.readline

N = int(input()) # 컴퓨터 갯수

field = [[0] * N for _ in range(N)] # 컴퓨터 상호 연결 관리 배열

chk = [[False] * N for _ in range(N)] # 방문 여부

hasVirus = [False] * N # 바이러스 감염 여부

for _ in range(int(input())) : # 입력값에 따른 상호 연결 체크
    pc1, pc2 = map(int, input().split())
    field[pc1 - 1][pc2 - 1] = 1
    field[pc2 - 1][pc1 - 1] = 1

def bfs(y, x) :
    q = deque([(y, x)])

    cnt = 0 # 감염 컴퓨터

    while q :
        y, x = q.popleft()
        for i in range(N) :
            nx = i

            # 필드 범위 넘어가는 경우
            if (y < 0 or y >= N) or (nx < 0 or nx >= N) :
                continue

            # 연결되어 있지 않은 네트워크인 경우
            if field[y][nx] == 0 :
                continue

            # 네트워크 연결, 방문되지 않은 컴퓨터, 바이러스 감염컴퓨터인 경우
            if (field[y][nx] == field[nx][y]) and not(chk[y][nx]) and not(chk[nx][y]) and not(hasVirus[nx]) :
                hasVirus[nx] = True

                chk[y][nx] = True
                chk[nx][y] = True

                cnt += 1
                q.append((nx, y))

    return cnt # 감염 컴퓨터 수 반환

print(bfs(0, 0))
