def solution(my_string):
    alp = [0] * 52
    new_string = list(my_string)
    for i in new_string:
        if i.isupper():
            alp[ord(i)-65] += 1
        else:
            alp[ord(i)-71] += 1
    return alp