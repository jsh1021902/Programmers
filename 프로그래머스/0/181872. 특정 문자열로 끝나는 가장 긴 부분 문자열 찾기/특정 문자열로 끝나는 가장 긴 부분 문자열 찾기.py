def solution(myString, pat):
    return myString.rsplit(pat, 1)[0] + pat