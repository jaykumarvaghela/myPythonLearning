for i in range(int(input())):
    n = int(input())
    scores = input()
    a=0
    b=0
    final = int(n/2)+1
    for j in range(0,n*2):
        if j%2!=0:
            a+=int(scores[j])
        else:
            b+=int(scores[j])
        if a>=final or b>=final:
            print(j+1)
            break


        


    