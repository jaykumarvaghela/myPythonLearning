def main():
    t = int(input())
    ans = []
    for i in range(t):
        n = int(input())
        lst = sorted(list(map(int, input().split())))
        ans.append(str(2*(abs(lst[0]-lst[-1]))))

    print("\n".join(ans))


if __name__ == "__main__":
    main()