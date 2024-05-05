def solution(balls, share):
    return fac(balls) /  (fac(balls - share) * fac(share))


def fac(num) :
    sumNum = 1
    
    for i in range(1, num + 1) :
        sumNum *= i
    
    return sumNum