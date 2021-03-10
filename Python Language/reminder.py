t = int(input())

lst=[]
for i in range(t):
    lst.append(list(map(int, input().split())))

for i in lst:
    print(i[0]%i[1])