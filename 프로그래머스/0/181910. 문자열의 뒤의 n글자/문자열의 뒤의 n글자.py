def solution(my_string, n):
    answer = ''
    li_string = list(my_string)
    start = len(my_string) - n
    temp = []
    for i in range(start, len(my_string)):
        temp.append(li_string[i])
    answer = "".join(temp)
    return answer