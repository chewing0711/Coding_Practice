def solution(my_string):
    answer = []
    
    for i in list(my_string) :
        if i.isdigit() :
            answer.append(int(i))
    answer.sort()
    return answer