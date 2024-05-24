def solution(balls, share):
    num = 1
    for i in range(share):
        num *= (balls - i)
    denom = 1
    for i in range(1, share+1):
        denom *= i
    return num // denom