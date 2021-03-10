def fun(x):
    return x[::-1].lstrip('0')

def main():
    n = int(input())
    for i in range(n):
        print(fun(input()))


if __name__ == "__main__":
    main()