def solution(n, k):
    return n * 12000 + k * 2000 if n < 10 else n * 12000 + (k- (n//10)) * 2000