def fun(string):
    l = len(string)
    print(string)
    
    print([string[i:i+int(l/2)] for i in range(0, l)])


def main():
    n = int(input())

    for i in range(n):
        print(fun(input()))

if __name__ == "__main__":
    fun("rotor")