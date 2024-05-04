def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    answer = []
    for e in emergency:
        index = sorted_emergency.index(e) + 1
        answer.append(index)
    return answer