def solution(strArr):
    answer = []
    for idx, st in enumerate(strArr):
        if idx % 2 == 0:
            st = st.lower()
            answer.append(st)
        else:
            st = st.upper()
            answer.append(st)
    return answer