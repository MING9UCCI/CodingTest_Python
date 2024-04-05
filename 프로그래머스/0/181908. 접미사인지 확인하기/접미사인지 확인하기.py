def solution(my_string, is_suffix):
    result = 0
    temp = []
    for i in range(len(my_string)):
        temp.append(my_string[-i:])
        if my_string[-i:] == is_suffix:
            result = 1
            break
    return result