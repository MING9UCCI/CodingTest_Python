def solution(myString, pat):
    answer = 0
    new_str = myString.upper()
    new_pat = pat.upper()
    
    if len(new_str) >= len(new_pat):
        if new_pat in new_str:
            return 1
        else:
            return 0
    else:
        return 0