def solution(spell, dic):
    for d in dic:
        if not set(spell) - set(d):
            return 1
    return 2