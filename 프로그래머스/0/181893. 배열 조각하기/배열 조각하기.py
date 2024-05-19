def solution(arr, query):
    for i in range(len(query)):
        if i == 0 or i%2 == 0:
            del arr[query[i]+1:]
        else:
            del arr[:query[i]]
    return arr