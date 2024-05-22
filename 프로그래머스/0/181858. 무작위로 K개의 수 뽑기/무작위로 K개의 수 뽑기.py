def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer and len(answer) < k:
            answer.append(i)
    if len(answer) < k:
        for i in range(0, k - len(answer)):
            answer.append(-1)
    return answer