def solution(arr, n):
    if len(arr) % 2 == 0:
        for i, v in enumerate(arr):
            if i % 2 == 1:
                arr[i] = v + n
    else:
        for i, v in enumerate(arr):
            if i % 2 == 0:
                arr[i] = v + n
    return arr