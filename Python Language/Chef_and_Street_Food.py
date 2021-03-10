from math import floor
t = int(input())

for i in range(t):
    max = 0
    n = int(input())
    for i in range(n):
        s = list(map(int, input().split()))
        val = floor(s[1]/(s[0]+1))
        tmp = val*s[2]
        max = tmp if max<tmp else max
        
    print(int(max))