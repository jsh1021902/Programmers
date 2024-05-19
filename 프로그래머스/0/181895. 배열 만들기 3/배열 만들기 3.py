def solution(arr, intervals):
    answer = []
    for a, b in intervals:
        answer += arr[a:b+1]
    return answer