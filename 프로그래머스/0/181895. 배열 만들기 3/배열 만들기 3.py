def solution(arr, intervals):
    answer = []
    for i in range(2):
        for j in range(intervals[i][0], intervals[i][1]+1):
            answer.append(arr[j])
    return answer


# 다른 사람들의 코드를 보고 느낀 효율적인 모범 답안.
# def solution(arr, intervals):
#     s1, e1 = intervals[0]
#     s2, e2 = intervals[1]
#     return arr[s1:e1+1] + arr[s2:e2+1]