def solution(my_string):
    return sorted(int(num) for num in my_string if num.isdigit())