def solution(n):
    anser = 0
    
    for i in range(2, n + 1, 2) :
        anser += i
        
    return anser