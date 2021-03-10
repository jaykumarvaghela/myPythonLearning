t = int(input())

for i in range(t):
    n,ns = input().split()

    if ns=="INDIAN":
        limit = 200
    else:
        limit = 400
    
    
    n=int(n)
    laddus = 0
    for i in range(n):
        lst = list(map(str, input().split()))
        if "TOP_CONTRIBUTOR" in lst:
            laddus = laddus+300
        if "CONTEST_HOSTED" in lst:
            laddus = laddus+50
        if "CONTEST_WON" in lst:
            laddus = laddus + 300
            if int(lst[1])<=20:
                laddus = laddus + (20-int(lst[1]))
        if "BUG_FOUND" in lst:
            laddus = laddus + (int(lst[1]))


    print(int(laddus/limit))
        
