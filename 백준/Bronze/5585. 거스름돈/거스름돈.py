N = int(input()) #380
chg = 1000 - N #620
cnt = 0
while(chg != 0) :
    if(chg // 500 >= 1) :
        cnt += chg // 500
        chg %= 500
        #print(f"남은잔액:{chg}, 횟수:{cnt}")
    if(chg // 100 >= 1) :
        cnt += chg // 100
        chg %= 100
        ##print(f"남은잔액:{chg}, 횟수:{cnt}")
    if(chg // 50 >= 1) :
        cnt += chg // 50
        chg %= 50
        #print(f"남은잔액:{chg}, 횟수:{cnt}")
    if(chg // 10 >= 1) :
        cnt += chg // 10
        chg %= 10
        #print(f"남은잔액:{chg}, 횟수:{cnt}")
    if(chg // 5 >= 1) :
        cnt += chg // 5
        chg %= 5
        #print(f"남은잔액:{chg}, 횟수:{cnt}")
    if(chg // 1 >= 1) :
        cnt += chg // 1
        chg %= 1
        #print(f"남은잔액:{chg}, 횟수:{cnt}")
print(cnt)