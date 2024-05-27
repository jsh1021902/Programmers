def solution(score):
    answer = sorted([sum(i) for i in score], reverse = True)
    return [answer.index(sum(i))+1 for i in score]