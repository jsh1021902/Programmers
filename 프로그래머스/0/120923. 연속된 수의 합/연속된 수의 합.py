def solution(num, total):
    numbers = total // num - (num-1) // 2
    return list(range(numbers, numbers + num))