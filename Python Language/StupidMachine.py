t = int(input())

for i in range(t):
    n = int(input())
    lst=list(map(int, input().split()))
     
    l=lst[0]
    tokens = 0
    for i in lst:
        if l>i:
            l=i
        tokens=tokens+l



    print(tokens)