def solution(n):
    answer = [[0 for j in range(n)] for i in range(n)]
    move = [[0,1], [1,0], [0,-1], [-1,0]]
    x, y, m = 0, 0, 0
    for i in range(1, n**2 + 1):
        answer[y][x] = i
        if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
            m = (m+1) % len(move)
        y, x = y + move[m][0], x + move[m][1]
    return answer