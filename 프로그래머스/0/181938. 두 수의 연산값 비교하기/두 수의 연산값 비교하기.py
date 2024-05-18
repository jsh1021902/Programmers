def solution(a, b):
    tmp1 = int(f"{a}{b}")
    tmp2 = 2 * a * b
    return int(max(tmp1, tmp2))