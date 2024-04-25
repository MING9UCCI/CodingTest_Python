def solution(strArr):
    for idx, s in enumerate(strArr):
        isInclude = False
        for i in range(len(s)) :
            if s[i:].startswith("ad") :
                isInclude = True
        if isInclude == True:
            strArr[idx] = 0
    while 0 in strArr:
        strArr.remove(0)
    return strArr