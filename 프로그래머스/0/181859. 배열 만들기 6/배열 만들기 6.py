def solution(arr):
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0:
            answer.append(arr[i])
        else:
            if answer[-1] == arr[i]:
                answer.pop()
                i += 1
            else:
                answer.append(arr[i])
                i += 1
    if len(answer) == 0:
        return [-1]
    return answer