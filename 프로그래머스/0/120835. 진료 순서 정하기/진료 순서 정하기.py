def solution(emergency):
    answer1 = []
    answer2 = []
    
    answer2 = sorted(emergency) #3 24 76
    answer2.reverse()#76 24 3
    
    for i in emergency:
        answer1.append(answer2.index(i)+1)#1 2 3
    return answer1