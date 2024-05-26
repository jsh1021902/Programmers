def solution(array, n):
    array.sort()
    box = []
    for i in array:
        box.append(abs(i-n))
    answer = [array[box.index(min(box))]]
    if len(answer) > 1:
        return min(answer)
    return answer[0]