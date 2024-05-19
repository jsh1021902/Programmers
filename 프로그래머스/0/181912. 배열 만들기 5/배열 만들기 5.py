def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        if int(intStr[s:s+l]) > k :
            answer.append(int(intStr[s:s+l]))
    return answer