def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    for num in range(min(numer, denom), 0, -1):
        if numer % num == 0 and denom % num == 0:
            result = num
            break
    
    return numer/result, denom/result