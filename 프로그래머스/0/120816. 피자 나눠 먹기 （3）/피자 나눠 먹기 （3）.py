# def solution(slice, n):
#     answer = 0
#     cnt = 1
#     while 1:
#         if slice // n > 0:
#             return cnt
#         else: 
#             slice += slice
#             cnt += 1
def solution(slice, n):
    return (n + (slice - 1)) // slice