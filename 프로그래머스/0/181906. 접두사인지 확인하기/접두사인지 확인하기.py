def solution(my_string, is_prefix):
    result = 0
    temp = []
    for i in range(len(my_string)):
        temp.append(my_string[0:i+1])
        if my_string[0:i+1] == is_prefix:
            result = 1
    return result