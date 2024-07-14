a,b = map(int,input().split())
r = 1
while(b!=a):
    r+=1
    temp = b
    if b%10 == 1:
        b//=10
    elif b%2 == 0:
        b//=2
    
    if temp == b:
        print(-1)
        break
else:
    print(r)

# A, B = map(int, input().split())
# cnt = 1
# while (B != A):
#     if (B < A) :
#         break
        
#     B = list(str(B))
#     if (B[len(B)-1] == '1'):
#         B.pop()
#         cnt += 1
        
#     B = int(''.join(B))
#     if(B % 2 == 0) :
#         B //= 2
#         cnt += 1
# if (B < A) : print(-1)
# else : print(cnt)