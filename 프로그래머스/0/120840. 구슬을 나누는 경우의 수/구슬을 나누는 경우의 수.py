def solution(balls, share):
    answer = 0
    n_pac = 1
    f_pac = 1
    s_pac = 1
    for i in range(1, balls+1, 1):
        n_pac *= i
    for i in range(1, balls-share+1, 1):
        f_pac *= i
    for i in range(1, share+1, 1):
        s_pac *= i
    print(n_pac, f_pac, s_pac)
    answer = n_pac // (f_pac * s_pac)
    return answer