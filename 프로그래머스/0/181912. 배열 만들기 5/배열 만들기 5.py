def solution(intStrs, k, s, l):
    answer = []
    temp = ""
    for i in range(len(intStrs)):
        for j in range(s, s+l):
            temp += intStrs[i][j]
        if int(temp) > k:
            answer.append(int(temp))
            temp = ""
        else:
            temp = ""
    return answer

# 내가 보기에 더 나은 코드. 참고.
# def solution(intStrs, k, s, l):
#     answer = []

#     for intStr in intStrs:
#         substr = intStr[s:s+l]
#         num = int(substr)
#         if num > k:
#             answer.append(num)

#     return answer