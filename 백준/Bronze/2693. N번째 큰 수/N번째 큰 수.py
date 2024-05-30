for _ in range(int(input())) :
    array = list(map(int, input().split()))
    array.sort()
    print(array[-3])