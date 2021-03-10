n = int(input())
x,y = 0,0


for i in range(n):
    s,t = [int(x) for x in input().split()]

    if x<=s:
        x = s
    if y<=t:
        y = t

if (100000-x)*500>100000*(500-y):
    print((100000-x)*500)
else:
    100000*(500-y)
