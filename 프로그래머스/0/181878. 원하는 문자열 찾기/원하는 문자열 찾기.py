def solution(myString, pat):
    if pat.upper() in myString.upper():
        answer = 1
    else:
        answer = 0
    return answer