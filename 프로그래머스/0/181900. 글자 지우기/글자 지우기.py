def solution(my_string, indices):
    answer = ''
    for index, val in enumerate(my_string):
        if index not in indices:
            answer += val
    return answer