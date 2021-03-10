def fun(number):
    sum = 0
    while number>1:
        sum  = sum+(int(number/5))
        number = int(number/5)
    
    return sum



def main():
    n = int(input())

    for i in range(n):
        print(fun(int(input())))


if __name__ == "__main__":
    main()