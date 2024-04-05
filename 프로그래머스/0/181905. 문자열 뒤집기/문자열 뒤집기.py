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


# 다른 사람의 풀이에서 이런 코드 보고 '아하 이런 방법이 있었다니'라고 생각함
# def solution(my_string, s, e):
#     return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]