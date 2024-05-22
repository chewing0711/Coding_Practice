"""
1. 아이디어
- 2중 for > 값이 1 && 방문 x > BFS실행
- BFS를 돌면서 그림의 개수 += 1, 최대값 갱신

2. 시간 복잡도
- BFS : O(V + E)
 V : m * n = 500 * 500
 E : v * 4 = 4 * 500 * 500
 V + E : 5 * 250000 = 100만, 컴퓨터는 초당 2억개의 연산이 가능하므로 최대 1초 이내로 프로그램이 종료 << 가능

3. 자료구조
- 그래프 지도 : int[][]
- 방문 여부 : bool[][]
- Queue(BFS)

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n )]
chk = [[False] * m for _ in range(n)]

cnt = 0 #
maxv = 0 # 최대값

# 우 하 상 좌가 표현된거
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x) :
    rs = 1

    q = [(y, x)]
    while q : # 큐가 새로 들어가지 않을 때 까지 연산을 반복
        ey, ex = q.pop()
        for k in range(4) :
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m : # 지도를 넘어간지 여부
                if map[ny][nx] == 1 and chk[ny][nx] == False :
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))

    return rs


for j in range(n) :
    for i in range(m) :
        if map[j][i] == 1 and chk[j][i] == False :
            # 방문을 했기 때문에 변경
            chk[j][i] = True

            # 전체 그림 갯수를 += 1
            cnt += 1

            # BFS를 통해서 그림의 크기를 구함
            maxv = max(maxv, bfs(j, i))

            # 최대값을 갱신 해줘야함

print(cnt)
print(maxv)