N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
ans_T = 0
ans_P = N // P
ans_PC = N % P

for idx, num in enumerate(size):
    if (num != 0):
        if (num % T == 0):
            ans_T += num // T
        else:
            ans_T += num // T + 1
       
print(ans_T)
print(ans_P, ans_PC)