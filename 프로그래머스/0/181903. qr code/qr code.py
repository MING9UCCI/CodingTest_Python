def solution(q, r, code):
    answer = ''
    for idx, val in enumerate(code): 
        if idx % q == r: answer += val
    return answer

# 어제 다른 사람의 코드에서 본 'enumerate'가 기억나서, 이를 이용하여 내 나름의 숏코딩을 해 보았다.