def solution(polynomial):
    answer = ''
    add = 0
    num = 0
    polynomial = polynomial.replace(' ', '').split('+')
    for i in polynomial:
        if i[-1] == 'x':
            num += 1 if len(i) == 1 else int(i[:-1:])
        else:
            add += int(i)
    if num > 0:
        answer = (str(num) if num > 1 else '') + 'x' + (' + ' if add > 0 else '')
    answer += (str(add) if add > 0 else '')
    return answer