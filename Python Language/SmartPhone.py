def fun(n,lst):
    m=0
    lst = sorted(lst)
    for i in lst:
        if m<(i*n):
            m = i*n

        n=n-1
    return m



def main():
    n = int(input())
    lst = []

    for i in range(n):
        lst.append(int(input()))

    print(fun(n,lst))
    

if __name__ == "__main__":
    main()