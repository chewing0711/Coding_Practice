def solution(s):
    answer = ''
    
    for i in set(s) :
        if s.count(i) == 1 :
            answer += i
            
    answer = list(answer)
    answer.sort()
    
    answer = ''.join(answer)
    
    return answer