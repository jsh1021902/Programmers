def solution(strArr):
    for i, v in enumerate(strArr):
        if i % 2 == 0:
            strArr[i] = v.lower()
        else:
            strArr[i] = v.upper()
    return strArr