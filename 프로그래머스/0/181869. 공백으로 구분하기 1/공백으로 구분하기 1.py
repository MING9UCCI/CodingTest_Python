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