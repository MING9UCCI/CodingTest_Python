def solution(arr, query):
    for idx, query in enumerate(query):
        if idx % 2 == 0:
            arr = arr[:query+1]
        else:
            arr = arr[query:]
    return arr
