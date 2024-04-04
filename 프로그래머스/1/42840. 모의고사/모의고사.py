def solution(answers):
    result = []
    ans_len = len(answers)
    score = []
    std = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for std_n in std:
        temp = 0
        cnt = 0
        for i in range(ans_len):
            if answers[i] == std_n[temp]:
                cnt += 1
                temp += 1
            else:
                temp += 1
            if temp >= len(std_n):
                temp = 0
        score.append(cnt)
    max_num = max(score)
    for i in range(3):
        if score[i] == max_num:
            result.append(i+1)
            
    return result