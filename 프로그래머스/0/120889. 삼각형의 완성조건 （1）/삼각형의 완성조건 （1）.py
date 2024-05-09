def solution(sides):
    sides.sort()
    return 2 if sides[2] >= sides[0] + sides[1] else 1