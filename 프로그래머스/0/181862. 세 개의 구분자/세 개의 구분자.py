def solution(myStr):
    myStr2 = []
    myStr3 = []
    myStr4 = []
    
    myStr = myStr.split('a')
    for i in myStr:
        myStr2 = i.split('b')
        for j in myStr2:
            if j != '':
                myStr3.append(j)
                
    for k in myStr3:
        myStr3 = k.split('c')
        for l in myStr3:
            if l != '':
                myStr4.append(l)
                
    if len(myStr4) == 0:
        myStr4.append('EMPTY')
    else:
        myStr4
    return myStr4