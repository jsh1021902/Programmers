def solution(myString):
    char = "abcdefghijk"
    for alp in char:
        myString = myString.replace(alp, 'l')
    return myString