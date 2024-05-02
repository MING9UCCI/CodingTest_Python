def solution(hp):
    answer = 0
    five = hp // 5
    three = (hp % 5) // 3
    one = (hp % 5 % 3) // 1
    answer = five + three + one
    return answer