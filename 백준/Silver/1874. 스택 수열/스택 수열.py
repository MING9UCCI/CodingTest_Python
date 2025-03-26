import sys

n = int(sys.stdin.readline().strip())
stack = []  
result = []  
temp = 1  

for _ in range(n):
    k = int(sys.stdin.readline().strip())

    while temp <= k:
        stack.append(temp)
        result.append("+")  
        temp += 1

    if stack[-1] == k:
        stack.pop()
        result.append("-")  
    else:
        print("NO")  
        exit()

print("\n".join(result))
