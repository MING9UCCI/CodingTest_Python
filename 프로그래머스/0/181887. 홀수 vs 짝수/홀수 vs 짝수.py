def solution(num_list):
    answer = 0
    odd_sum = 0
    even_sum = 0
    for idx, num in enumerate(num_list):
        if idx % 2 == 0:
            odd_sum += num
        else:
            even_sum += num
    if odd_sum >= even_sum:
        return odd_sum
    else:
        return even_sum