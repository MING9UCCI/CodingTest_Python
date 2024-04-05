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