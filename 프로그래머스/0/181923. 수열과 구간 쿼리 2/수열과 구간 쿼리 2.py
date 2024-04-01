def solution(arr, queries):
    result = []
    for i in range(len(queries)):
        min = 1000000
        for j in range(queries[i][0], queries[i][1]+1, 1):
            if arr[j] > queries[i][2]:
                if min > arr[j]:
                    min = arr[j]
        if min == 1000000:
            result.append(-1)
        else:
            result.append(min)
    return result