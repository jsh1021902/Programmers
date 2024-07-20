def DFS(n, order, numbers, target):
    if order == len(numbers)-1:
        if n == target:
            return 1
        return 0
    
    case1 = DFS(n+numbers[order+1], order+1, numbers, target)
    case2 = DFS(n-numbers[order+1], order+1, numbers, target)
    
    return case1 + case2

def solution(numbers, target):
    return DFS(numbers[0], 0, numbers, target) + DFS(-numbers[0], 0, numbers, target)