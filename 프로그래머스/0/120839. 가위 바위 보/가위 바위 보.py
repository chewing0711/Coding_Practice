def solution(rsp):
    answer = ""
    
    for i in list(rsp) :
        if i == "0" :
            answer += "5"
        elif i == "2" :
            answer += "0"
        elif i == "5" :
            answer += "2"
            
    return answer