def solution(array):
    answer = 0
    array.sort()
    length = len(array) // 2
    answer = array[length]
    return answer