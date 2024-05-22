def solution(rank, attendance):
    choice = []
    a = 0
    b = 0
    c = 0
    
    for i, v in enumerate(rank):
        if attendance[i]:
            choice.append(rank[i])
    choice.sort()
    
    for i, v in enumerate(rank):
        if v == choice[0]:
            a = i
        elif v == choice[1]:
            b = i
        elif v == choice[2]:
            c = i
            
    return 10000 * a + 100 * b + c