def solution(a, b):
    answer = 0
    tmp1 = int(str(a) + str(b))
    tmp2 = int(str(b) + str(a))
    
    if tmp1 > tmp2:
        answer = tmp1
    else:
        answer = tmp2
    return answer