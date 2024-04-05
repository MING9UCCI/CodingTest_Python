from collections import deque

def solution(my_string, s, e):
    answer = ''
    dq = deque()
    for i in range(s, e+1):
        dq.appendleft(my_string[i])
    
    cnt = 0
    for i in range(len(my_string)):
        if i >= s and i <= e:
            answer += dq[cnt]
            cnt += 1
        else:
            answer += my_string[i]
    return answer