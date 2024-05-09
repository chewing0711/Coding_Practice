def solution(my_string) :
    answer = ""
    
    for i in range(len(my_string)) :
        if not(my_string[i] in answer) :
            answer += my_string[i]
    
    return answer