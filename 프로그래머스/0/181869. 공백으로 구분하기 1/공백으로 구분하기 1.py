def solution(my_string):
    result = []
    string = ""
    for s in my_string:
        if s == " ":
            result.append(string)
            string = ""
        else:
            string += s
    result.append(string)
    return result

# def solution(my_string):
#     return my_string.split(' ')
# 이 간단한 방법을 왜 생각 못했을까 ㅎㅎ;;