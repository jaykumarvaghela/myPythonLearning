def addition(n):
    sum = 0
    for i in range(len(n)):
        sum = sum+int(n[i])

    return sum


def main():
    t = int(input())

    dict={}
    for i in range(t):
        dict[i] = str(input())


    for i in dict:
        print(addition(dict[i]))

if __name__ == '__main__':
    main()