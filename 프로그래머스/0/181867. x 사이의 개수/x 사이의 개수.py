def solution(myString):
    answer = []
    arr = myString.split('x')
    for i in arr:
        answer.append(len(i))
    return answer