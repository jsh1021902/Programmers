def solution(M, N):
    return 0 if M and N == 1 else (M-1) + M * (N-1)