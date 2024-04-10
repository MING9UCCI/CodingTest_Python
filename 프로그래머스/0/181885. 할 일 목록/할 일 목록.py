def solution(todo_list, finished):
    answer = []
    for idx, li in enumerate(finished):
        if li == False:
            answer.append(todo_list[idx])
    return answer