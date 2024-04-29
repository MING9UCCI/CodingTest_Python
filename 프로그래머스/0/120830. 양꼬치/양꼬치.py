def solution(n, k):
    answer = 0
    ser = n // 10
    answer = n * 12000 + (k-ser) * 2000
    return answer