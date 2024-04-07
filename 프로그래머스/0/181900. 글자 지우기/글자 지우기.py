def solution(my_string, indices):
    answer = ''
    new_string = list(my_string)
    for i in indices:
        new_string[i] = 0
    while 0 in new_string:
        new_string.remove(0)
    answer += "".join(new_string)
    return answer

# 그저 새로운 배열을 만들고, 하나씩 지워가면서 결과값을 출력하면 되는 줄 알았다. 하지만 배열의 크기 또한 줄어드는 것을 고려하지 못해, 다른 방법을 찾게 되었다. 좀 특이하지만 배열의 크기는 유지하기 위해 indices 값에 해당 되는 항목을 0으로 변경 한 후, 0을 한꺼번에 삭제하는 방법을 생각하게 되었다.