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


# def solution(my_string):
#     answer = []
#     for i in range(len(my_string)):
#         answer.append(my_string[-i:])
#     answer.sort()
#     return answer

#사실 이렇게 간단하게 짜고 싶었지만, queue를 사용해 보고 싶었다.