def solution(strArr):
    length = [len(i) for i in strArr]
    answer = []
    for j in set(length):
        answer.append(length.count(j))
    return max(answer)