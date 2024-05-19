def solution(numLog):
    result = ''
    for i in range(1, len(numLog)):
        if numLog[i] - numLog[i - 1] == 1:
            result += 'w'
        elif numLog[i - 1] - numLog[i] == 1:
            result += 's'
        elif numLog[i] - numLog[i - 1] == 10:
            result += 'd'
        elif numLog[i - 1] - numLog[i] == 10:
            result += 'a'
    return result