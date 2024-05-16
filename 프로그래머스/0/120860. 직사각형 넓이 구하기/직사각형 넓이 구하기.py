def solution(dots):
    dots.sort()
    return (abs(dots[3][0] - dots[0][0])) * (abs(dots[3][1] - dots[0][1]))