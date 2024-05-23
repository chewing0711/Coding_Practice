"""
1. 아이디어
 - 2중 반복문으로 돌다가 아직 들리지 않고, 1인 경우에 정수 값을 증가, 더 움직이지 못하면 정수값을 배열에 저장 후 0으로 초기화
 
2. 시간 복잡도
 - BFS는 O(V + E)
 - V = n * n = 25 * 25 = 625
 - E = V * 4 = 625 * 4
 - V + E = 625 * 2500 = 1,562,500 => 2억보다 낮음 => 1초 이내로 처리 가능?
 
3. 자료구조
 - 필드 : field = int[][]
 - 방문 여부 : chk = bool[][]
 - 방문한 적 있는 좌표 저장 : queue(BFS)
 - 단지 크기 저장 : int[]
 
"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # 크기 입력

field = [list(map(int, input().rstrip())) for _ in range(n)] # 전체 지도 초기화
chk = [[False] * n for _ in range(n)] # 체크된 여부

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
homes = [] # 단지의 집들 수 저장

def bfs(y, x) :
    q = deque([(y, x)]) # 큐 생성
    rs = 1 # 단지 크기 저장

    while q :
        y, x = q.popleft() # 좌표 하나 반환

        for i in range(4) : # 4방향으로 확인
            ny = y + dy[i]
            nx = x + dx[i]

            if (ny < 0 or ny >= n) or (nx < 0 or nx >= n) : # 필드 범위 초과
                continue

            if field[ny][nx] == 0 : # 0인 경우 확인 안함
                continue

            if not(chk[ny][nx]) : # 방문 여부 체크
                chk[ny][nx] = True # 방문한 적 있는 걸로 변경

                rs += 1 # 단지의 크기 증가

                q.append((ny, nx)) # 현재 위치 큐에 추가
    return rs


for j in range(n) :
    for i in range(n) : # 필드 2차원 배열로 탐색
        if field[j][i] == 1 and chk[j][i] == False : # 현재 반복문이 보는 좌표가 집인지, 방문한 적 없는지 확인
            chk[j][i] = True

            cnt += 1 # 단지 수 증가
            homes.append(bfs(j, i)) # 단지 크기 저장

homes.sort() # 정렬
print(cnt)
for i in homes :
    print(i)