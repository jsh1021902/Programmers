def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if "ad" not in strArr[i]: 
            answer.append(strArr[i])
    return answer