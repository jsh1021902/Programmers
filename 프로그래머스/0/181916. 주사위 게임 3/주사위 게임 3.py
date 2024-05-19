def solution(a, b, c, d):
    answer = 0
    dice = [a, b, c, d]
    arr = list(set(dice))
    
    if len(arr) == 4:
        answer = min(arr)
    elif len(arr) == 3:
        p = max(dice, key=dice.count)
        tmp = [num for num in arr if num != p]
        answer = tmp[0] * tmp[1]
    elif len(arr) == 2:
        if max([dice.count(num) for num in arr]) > 2:
            p = max(dice, key=dice.count)
            q = min(dice, key=dice.count)
            answer = ((10 * p) + q)**2
        else:
            answer = ((arr[0] + arr[1]) * abs(arr[0] - arr[1]))
    elif len(arr) == 1:
        answer = int(str(arr[0]) * 4)
    
    return answer