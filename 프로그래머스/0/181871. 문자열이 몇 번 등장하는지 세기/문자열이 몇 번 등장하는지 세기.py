def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        target = myString[i:i+len(pat)]
        if len(target) != len(pat):
            break
        if target == pat:
            answer += 1
    return answer