def solution(my_strings, parts):
    answer = ''
    for index, val in enumerate(parts):
        answer += my_strings[index][val[0]:val[1]+1]
    return answer