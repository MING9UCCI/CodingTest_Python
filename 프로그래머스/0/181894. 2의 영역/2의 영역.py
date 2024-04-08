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

# 좀 길고 살짝 더럽게 짜진 것 같아서 아쉽다. 좀 더 공부를 해야겠다!!