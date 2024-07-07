def solution(n, lost, reserve):    
    # 여벌 체육복을 가져왔지만 도난당한 학생들을 제거
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
            
    # 체육복 빌려주기
    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set.remove(i - 1)
        elif i + 1 in lost_set:
            lost_set.remove(i + 1)
    return n - len(lost_set) # 수업을 들을 수 있는 학생 수 계산