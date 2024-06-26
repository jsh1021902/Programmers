def solution(arr, queries):
    result = []
    
    for query in queries:
        answer = []
        for i in range(query[0], query[1] + 1):
            if arr[i] > query[2]:
                answer.append(arr[i])
        result.append(-1 if not answer else min(answer))
        
    return result