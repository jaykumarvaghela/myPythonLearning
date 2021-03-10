t = int(input())

while t!=0:
    g,p = [int(x) for x in input().split()]
    n = int(input())
    o = 0
    t = 0
    for i in range(n):
        l,m = [int(x) for x in input().split()]
        if l == 1:
            t +=1
        if m == 1:
            o+=1
    
    print((max(g,p)*min(t,o))+(min(g,p)*max(o,t)))

    t-=1