def dfs(v, computers, visited):
    visited[v] = True

    for i in range(len(computers[v])):
        if computers[v][i] == 1 and visited[i] == False:
            dfs(i, computers, visited)
            
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited)
            answer += 1
        
    return answer