t = int(input())

for i in range(t):
    m = int(input())
    a = set(map(int, input().split()))
    
    n = int(input())
    b = set(map(int, input().split()))

    f = 0
    if all(i in b for i in a):
        f=1

    print(True if f==1 else False)
