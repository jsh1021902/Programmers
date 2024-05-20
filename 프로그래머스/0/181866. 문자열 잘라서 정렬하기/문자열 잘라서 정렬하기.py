def solution(myString):
    answer = [string for string in myString.split("x") if string != ""]
    answer.sort()
    return answer