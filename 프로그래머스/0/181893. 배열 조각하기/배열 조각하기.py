# def solution(arr, query):
#     for idx, num in enumerate(query):
#         if num % 2 == 0:
#             arr = arr[:num+1]
#         else:
#             arr = arr[num:]
#     return arr


def solution(arr, query):
    for i, query in enumerate(query):
        if i % 2 == 0:
            arr = arr[:query+1]
        else:
            arr = arr[query:]
    return arr
