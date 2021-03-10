def main():
    n = int(input())

    while n!=0:
        number = input()
        print(int(number[0])+int(number[-1]))
        n=n-1


if __name__ == "__main__":
    main()