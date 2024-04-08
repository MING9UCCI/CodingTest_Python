def solution(arr):
    answer = []
    start, end = -1, -1
    for idx, num in enumerate(arr):
        if num == 2:
            if start == -1:
                start = idx
            else:
                end = idx
    if start == -1 and end == -1:
        answer.append(-1)
        return answer
    elif start != -1 and end == -1:
        answer.append(2)
        return answer
    for i in range(start, end+1):
        answer.append(arr[i])
    return answer