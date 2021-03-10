import numpy

def main():
    n,m = input().split()

    a = numpy.array(map(int, input().split()))
    b = list(map(int, input().split()))


    print(a,b)


if __name__ == "__main__":
    main()