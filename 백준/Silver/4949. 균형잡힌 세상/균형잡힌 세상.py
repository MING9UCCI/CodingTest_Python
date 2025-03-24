while True:
    s = input()
    if s == ".":
        break  # 종료 조건

    stack = []
    balanced = True

    for char in s:
        if char == "(" or char == "[":
            stack.append(char)  # 열린 괄호는 스택에 추가
        elif char == ")" or char == "]":
            if stack:
                top = stack.pop()  # 스택에서 꺼낸 괄호와 비교
                if (char == ")" and top != "(") or (char == "]" and top != "["):
                    balanced = False
                    break
            else:
                balanced = False
                break

    if stack:
        balanced = False  # 스택에 남아 있는 열린 괄호가 있으면 불균형

    if balanced:
        print("yes")
    else:
        print("no")