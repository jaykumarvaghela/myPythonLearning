d = {"G":"C", "C":"G","T":"A","A":"U"}
inp = input()
n=""
for i in inp:
    if i in d:
        n=n+d[i]
    else:
        n="Invalid Input"
        break
print(n)