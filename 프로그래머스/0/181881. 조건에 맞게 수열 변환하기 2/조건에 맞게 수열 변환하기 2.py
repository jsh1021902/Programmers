def solution(arr):
    index = 0
    
    while True:
        change = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                change.append(int(i / 2))
            elif i < 50 and i % 2 == 1:
                change.append(i * 2 + 1)
            else:
                change.append(i)
        
        same = all(a == b for a, b in zip(arr, change))
        if same:
                break

        index += 1
        arr = change
    return index