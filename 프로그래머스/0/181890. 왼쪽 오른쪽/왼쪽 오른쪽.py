def solution(str_list):
    answer = []
    cnt = 0
    for i, ch in enumerate(str_list):
        if ch == "l":
            answer = str_list[:i]
            cnt += 1
            return answer
        if ch == "r":
            answer = str_list[i+1:]
            cnt += 1
            return answer
    if cnt == 0:
        return answer
            