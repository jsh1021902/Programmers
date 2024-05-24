def solution(array):
    while len(array) != 0:
        for i, v in enumerate(set(array)):
            array.remove(v)
        if i == 0:
            return v
    return -1