w, t = input().split()
w=int(w)
t=float(t)

if w%5!=0:
    print("%.2f"%t)

else:
    if (w+0.50)>t:
        print("%.2f"%t)
    else:
        print("%.2f"%(t-(w+0.50)))