def solution(myString, pat):
    string = ''
    for i in myString:
        if i == 'A':
            string += 'B'
        else:
            string += 'A'
            
    if pat in string:
        return 1
    else:
        return 0
    return 0