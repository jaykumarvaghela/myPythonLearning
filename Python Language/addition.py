n = int(input())

lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))

for i in range(len(lst)):
    print(sum(lst[i]))