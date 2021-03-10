def main():
    n = int(input())
    m=n

    for i in range(n-1):
        l = " ".join(str(i+2)*(i+1))
        print(l.center(n+(int(n/2))))

    while n!=1:
        l = " ".join(str(n)*(n-1))
        print(l.center(m+(int(m/2))))
        n=n-1

    
    

if __name__ == "__main__":
    main()