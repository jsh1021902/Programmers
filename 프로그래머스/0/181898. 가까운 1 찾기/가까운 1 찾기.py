def solution(arr, idx):
    answer = 0
    answer_list = []
    
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            answer_list.append(i)
    
    if len(answer_list) == 0:
        answer = -1
    else:
        answer = min(answer_list)
    return answer