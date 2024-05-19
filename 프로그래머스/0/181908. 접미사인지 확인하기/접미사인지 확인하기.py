def solution(my_string, is_suffix):
    answer_list = []
    
    for i in range(len(my_string)):
        answer_list.append(my_string[i:])
    
    return 1 if is_suffix in answer_list else 0