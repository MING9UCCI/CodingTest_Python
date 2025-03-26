import sys
input = sys.stdin.readline

def custom_round(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)

n = int(input().strip())
if n == 0:
    print(0)
    exit()

li = [int(input().strip()) for _ in range(n)]
temp = custom_round(n * 0.15)

li.sort()
li = li[temp:] if temp == 0 else li[temp:-temp]

if len(li) == 0:
    print(0)
else:
    avg = custom_round(sum(li) / len(li))
    print(avg)
