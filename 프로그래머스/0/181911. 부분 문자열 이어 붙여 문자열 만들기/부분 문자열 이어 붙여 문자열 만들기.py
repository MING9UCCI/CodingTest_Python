def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        li_word = list(my_strings[i])
        for j in range(parts[i][0], parts[i][1]+1):
            answer += li_word[j]
    return answer