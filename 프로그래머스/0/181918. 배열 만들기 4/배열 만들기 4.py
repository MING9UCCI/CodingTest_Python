def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            last = stk[len(stk)-1]
            if last < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
    return stk


# 1, 4, 2, 5, 3