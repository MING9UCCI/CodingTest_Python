def solution(arr, queries):
    result = [] #결과 제출을 위한 result 배열 생성
    for i in range(len(queries)): #queries의 값 만큼 반복, len(queries) = len(result)
        small = 1000000
        for j in range(queries[i][0], queries[i][1]+1, 1): #0 ~ 4까지 반복
            if arr[j] > queries[i][2]: #만약 j가 2보다 크다면
                if small > arr[j]:
                    small = arr[j]
        if small == 1000000:
            result.append(-1)
        else:
            result.append(small)
    return result