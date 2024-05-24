"""
1. 아이디어
 - 2중 반복문을 통해서 돌면서 해당 영역에서 4방향 중 더 이동할 곳이 없을 때 + 1

2. 시간 복잡도
 - BFS의 시간 복잡도는 O(V + E)
 - V : N * M = 50 * 50 = 2500
 - E : 4 * 2500 = 10000
 - V + E : 2500 * 10000 = 25,000,000 <= 2억보다 낮음

3. 자료구조
 - 필드 : int[][]
 - 방문 여부 : bool[][]
 - 필요 지렁이 수 : int

"""


import sys
from collections import deque

input = sys.stdin.readline

result = []

# 필요 지렁이의 수
cnt = 0

for _ in range(int(input())) :
    # 가로, 세로, 배추의 개수
    m, n, k = map(int, input().split())

    # 농장 초기화
    field = [[0] * m for _ in range(n)]

    # 방문 여부 체크를 위한 bool타입 배열
    chk = [[False] * m for _ in range(n)]

    # 4방향 탐색을 위한 리스트
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cnt = 0

    def bfs(y, x) :
        q = deque([(y, x)])

        while q :

            y, x = q.popleft()

            for i in range(4) : # 상하좌우 탐색을 위한 4번 반복
                ny = y + dy[i]
                nx = x + dx[i]

                if (0 > ny or ny >= n) or (0 > nx or nx >= m) :
                    continue

                if field[ny][nx] == 0 :
                    continue

                if not(chk[ny][nx]) :
                    chk[ny][nx] = True
                    q.append((ny, nx))

    for _ in range(k) : # 입력된 좌표에 배추(1)를 저장
        x, y = map(int, input().split())
        field[y][x] = 1

    for j in range(n) : # 2차원 반복문을 통해서 접근
        for i in range(m) :
            if (field[j][i] == 1) and not(chk[j][i]) :
                chk[j][i] = True # 방문 했음으로 변경

                cnt += 1 # 필요 수 증가

                bfs(j, i) # 함수 실행

    result.append(cnt) # 이번 케이스 결과값 저장

for i in result :
    print(i)