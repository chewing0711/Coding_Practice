def solution(numbers, k):
    idx = 0
    check = []
    
    for i in range(k) :
        idx += 2
        
        if idx >= len(numbers) :
            idx -= len(numbers)
            
        check.append(idx + 1)
            
    return check[-2]