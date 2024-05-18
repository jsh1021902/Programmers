def solution(a, b, flag):
    answer = 0
    if flag:
        answer = int(a + b)
    else:
        answer = int(a - b)
    return answer