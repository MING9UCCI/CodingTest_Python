def solution(num_list):
    last = len(num_list) - 1
    if num_list[last] > num_list[last-1]:
        num_list.append(num_list[last] - num_list[last-1])
    else:
        num_list.append(num_list[last] * 2)
    return num_list