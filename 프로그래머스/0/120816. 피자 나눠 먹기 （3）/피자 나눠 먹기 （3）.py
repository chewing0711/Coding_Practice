def solution(slice, n):
    return 1 + (n // slice) if n % slice != 0 else (n // slice)