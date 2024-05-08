def solution(n):
    answer = []
    
    i = 2
    while i <= (n + 1):
        if n % i == 0 :
            n = n // i
            answer.append(i)
        else :
            i += 1
    
    answer = list(set(answer))
    answer.sort()
        
    return answer