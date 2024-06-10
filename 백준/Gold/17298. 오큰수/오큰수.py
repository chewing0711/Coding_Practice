import sys

input = sys.stdin.readline

n = int(input())
ans = [0] * n
A = list(map(int, input().split()))
Stack = []

for i in range(n) :
    while Stack and A[Stack[-1]] < A[i] : # 오큰수 조건
        ans[Stack.pop()] = A[i] # 정답 리스트에 오큰수 저장
    Stack.append(i)

while Stack :
    ans[Stack.pop()] = -1

for i in ans :
    print(i, end = ' ')
