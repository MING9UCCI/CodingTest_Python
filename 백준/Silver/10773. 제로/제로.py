arr = []

k = int(input())
for i in range(k):
    s = int(input())
    if s == 0:
        if arr: # arr이 빈 경우일 수도 있으니까
            arr.pop()
    else:
        arr.append(s)

print(sum(arr))