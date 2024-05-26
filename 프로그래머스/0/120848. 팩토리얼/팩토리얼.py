def solution(n):
    answer = 1
    factorial = 1
    while n >= factorial:
        answer += 1
        factorial = answer * factorial
    answer = answer - 1
    return answer