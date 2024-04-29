def solution(my_string, n):
    answer = ''
    li_string = list(my_string)
    for i in range(len(my_string)):
        answer += my_string[i] * n
    return answer