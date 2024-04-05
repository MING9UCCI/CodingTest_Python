from collections import deque

def solution(my_string):
    answer = []
    queue = deque(list(my_string))
    for i in range(len(my_string)):
        temp = "".join(queue)
        answer.append(temp)
        queue.popleft()
    answer.sort()
    return answer