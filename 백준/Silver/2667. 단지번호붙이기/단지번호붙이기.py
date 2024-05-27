import sys

input = sys.stdin.readline

N = int(input())

field = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x):
    global each
    each += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < N:
            if field[ny][nx] == 1 and not chk[ny][nx]:
                chk[ny][nx] = True
                dfs(ny, nx)

for j in range(N):
    for i in range(N):
        if field[j][i] == 1 and not chk[j][i]:
            each = 0  # each 변수를 여기서 초기화합니다.
            chk[j][i] = True
            dfs(j, i)
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)
