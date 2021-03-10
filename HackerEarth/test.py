s = "abdba"
l = len(s)

print(sorted(s[:int(l/2)])==sorted(s[int(l/2)+1:]))