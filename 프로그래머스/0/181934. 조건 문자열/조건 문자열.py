def solution(ineq, eq, n, m):
    answer = 0
    if eq == "!":
        if ineq == "<":
            answer = int(n<m)
        else:
            answer = int(n>m)
    else:
        if ineq == "<":
            answer = int(n<=m)
        else:
            answer = int(n>=m)
    return answer