def solution(box, n):
    width = box[0] // n
    length = box[1] // n
    height = box[2] // n
    result = width * length * height
    return result
    


# 가로 10, 세로 8, 높이 6
# 10을 3으로 나누고 8을 3으로 나누고 이 것을 곱하면, 3 * 2 = 6
# 6을 3으로 나누면 2, 앞에서 나온 값이랑 곱하면 6 * 2 = 12

