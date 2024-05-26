def solution(my_string):
    return sum(int(num) for num in my_string if num.isdigit())