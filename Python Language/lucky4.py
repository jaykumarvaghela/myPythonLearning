from collections import Counter

def fun(x):
    count = Counter(x)
    return 0 if "4" not in count else count["4"]


def main():
    n = int(input())
    for i in range(n):
        print(fun(input()))

if __name__ == "__main__":
    main()