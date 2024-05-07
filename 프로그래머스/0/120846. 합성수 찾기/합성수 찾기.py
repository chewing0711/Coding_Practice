def solution(n):
    answer = 0
    
    for i in range(4, n + 1) :
        answer += check(i)
    
    return answer

def check(num) :
    for i in range(2, num) :
        if num % i == 0 :
            return 1
    return 0