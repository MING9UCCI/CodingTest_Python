def solution(my_string, index_list):
    answer = ''
    new = list(my_string)
    for i in index_list:
        answer += new[i]
    return answer