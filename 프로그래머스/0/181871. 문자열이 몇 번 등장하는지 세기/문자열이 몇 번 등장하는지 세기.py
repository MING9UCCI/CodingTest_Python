def solution(myString, pat):
    answer = 0
    for idx, s in enumerate(myString): #myString을 인덱스와 문자열을 쪼개서 s에 담음 (1: idx = 0, s = b)
        if s == pat[0] and idx < len(myString) - len(pat) + 1: #myString의 한 문자가 pat의 첫 문자와 동일 할 경우 (1: b != a), myString에서 pat의 길이가 안 들어갈 경우 제외
            count = 0
            for j in range(len(pat)):# pat의 길이만큼 반복. (1: 0, 1, 2)
                if myString[idx+j] == pat[j]:
                    count += 1
            if count == len(pat):
                answer += 1
    return answer