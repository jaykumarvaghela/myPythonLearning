s = "abbtta"


n=len(s)
l=[]
while n!=0:
    l.append(s[n-1])
    n=n-1

s1="".join(l)

if s==s1:
    print("Yes")

else:
    print("no")