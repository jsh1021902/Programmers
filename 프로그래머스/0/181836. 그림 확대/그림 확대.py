def solution(picture, k):
    answer = []
    for i in picture:
        char = ''
        for j in i:
            char += j * k
        for a in range(k):
            answer.append(char)
    return answer