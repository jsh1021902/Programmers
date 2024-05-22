def solution(arr):
    x = len(arr)
    y = len(arr[0])
    
    if x > y:
        for i in range(x):
            for j in range(x-y):
                arr[i].append(0)
    elif x < y:            
         for i in range(y-x):
                arr.append([0] * len(arr[0]))
    else:
         return arr       
    return arr