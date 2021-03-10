t = int(input())

for i in range(t):
    s = input()
    l = len(s)

    if l%2==0:
        #even
        ans = sorted(s[:int(l/2)])==sorted(s[int(l/2):])
        print("YES" if ans==True else "NO")

    else:
        #odd
        ans = sorted(s[:int(l/2)])==sorted(s[int(l/2)+1:])
        print("YES" if ans==True else "NO")
