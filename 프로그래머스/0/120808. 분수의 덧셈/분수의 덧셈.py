def solution(numer1, denom1, numer2, denom2):
    numer = denom1 * numer2 + denom2 * numer1
    denom = denom1 * denom2
    div = GCD(denom, numer)
    return [numer // div, denom // div]

def GCD(x, y) :
    while y > 0 :
        x, y = y, x % y
    return x