import numpy as np
def solution(people, limit):
    # 오름차순 정렬
    people.sort()
    
    # 사용된 구명보트 개수
    cnt = 0
    
    # index 지정
    left = 0
    right = len(people) - 1
    
    while left <= right:
        # 가장 무거운 사람이 제한의 절반이라면, 이제부터 다 두 명씩 탈 수 있음
        if people[right] <= limit / 2:
            cnt += np.ceil((right - left + 1) / 2)
            break
        # 가장 무거운 사람과 가장 가벼운 사람이 같이 탈 수 있으면
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        cnt += 1
    return cnt