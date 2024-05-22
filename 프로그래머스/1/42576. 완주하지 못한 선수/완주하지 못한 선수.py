def solution(participant, completion):
    import collections
    
    # 참가자를 카운트하는 딕셔너리 생성
    participant_count = collections.Counter(participant)
    # 완주자를 카운트해서 참가자 딕셔너리에서 차감
    for c in completion:
        participant_count[c] -= 1
        # 만약 카운트가 0이 되면 딕셔너리에서 제거
        if participant_count[c] == 0:
            del participant_count[c]
    
    # 딕셔너리에 남아 있는 한 명의 참가자를 반환
    return list(participant_count.keys())[0]
