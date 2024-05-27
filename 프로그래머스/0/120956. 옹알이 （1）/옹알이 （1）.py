def solution(babbling):
    answer = 0
    for i in babbling:
        count = 0
        word = ''
        for j in i:
            word += j
            if word in ["aya", "ye", "woo", "ma"]:
                word = ''
                count += 1
        if len(word) == 0 and count > 0:
            answer += 1
    return answer