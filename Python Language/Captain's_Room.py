from collections import Counter
n = int(input())
lst = map(int, input().split())

new = Counter(lst)

for i in new:
    if new[i]==1:
        print(i)

