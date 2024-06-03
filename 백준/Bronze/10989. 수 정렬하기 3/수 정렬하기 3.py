import sys

limit = int(sys.stdin.readline())
array = [0] * 10000

for _ in range(limit) :
    array[int(sys.stdin.readline()) - 1] += 1

for i in range(10000) :
    for k in range(array[i]) :
        print(i + 1)