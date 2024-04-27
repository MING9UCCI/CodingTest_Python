def solution(n):
    answer = 0
    pizza = 6
    while 1:
        if pizza % n == 0:
            return pizza // 6
        else:
            pizza += 6