def solution(n):
    return ((n * 6) / gcd(n, 6)) / 6

def gcd(num1, num2) :
    while num2 > 0 :
        num1, num2 = num2, num1 % num2
    
    return num1
    