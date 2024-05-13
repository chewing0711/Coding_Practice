def solution(n):
    n = list(str(n))
    answer = 0
    
    for i in n :
        answer += int(i)
        
    return answer