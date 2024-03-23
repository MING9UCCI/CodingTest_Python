def solution(a, d, included):
    sum = 0
    for i in range(len(included)):
        if i == 0:
            if included[i] == True:
                sum += a
        else:
            if included[i] == True:
                a += d
                sum += a
            else:
                a += d
    return sum