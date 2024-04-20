def solution(my_string, alp):
    answer = ""
    for i in my_string:
        if i == alp: 
            ch = i.upper()
            answer += ch
        else: answer += i
    return answer