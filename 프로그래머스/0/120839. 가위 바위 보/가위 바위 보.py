def solution(rsp):
    answer = ''
    li = list(rsp)
    for i in range(len(li)):
        if li[i] == '0':
            answer += '5'
        elif li[i] == '2':
            answer += '0'
        else:
            answer += '2'
    return answer