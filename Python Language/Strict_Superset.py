a = set(map(int, input().split()))
n = int(input())
lst=[]

for i in range(n):
    lst.append(set(map(int, input().split())))

for i in lst:
    ans = all(x in a for x in i)
    if ans==False:
        break
    
print(ans)