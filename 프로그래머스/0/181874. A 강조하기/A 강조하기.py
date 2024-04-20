def solution(myString):
    answer = ''
    for i in myString:
        if i == 'a' or i == 'A':
            n = i.upper()
            answer += n
        else:
            n = i.lower()
            answer += n
    return answer