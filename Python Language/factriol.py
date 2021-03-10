n = 5

def fac(n):
    if n==1:
        return n
    else:
        return n*fac(n-1)


def main():
    t = int(input())

    lst = []
    for i in range(t):
        lst.append(int(input()))

    for i in lst:
        print(fac(i))


if __name__ == "__main__":
    main()