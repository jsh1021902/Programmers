def solution(numlist, n):
    numlist = [(abs(n-num), -num) for num in numlist]
    numlist.sort()
    return [-num for _, num in numlist]