def solution(n):
    answer = 1
    i = 0
    
    while answer <= n :
        i += 1
        answer *= i
        
    return i - 1
