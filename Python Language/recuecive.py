n=int(input())
# Recurcive Function
def fun(n):
    if n==1:
        return n
    else:
        return n*fun(n-1)

print("Using Recursion : ",fun(n))

# Ittritation

fac=1
while n!=1:
    fac=fac*n
    n=n-1

print("Using iteration :",fac)

"""
Recursion :- In this process we call function again and again until the condition is not satisfied. We do not required any looping statement.
 
Iteration :- In this process we use looping statement only.

##
[+] pros and cons of an iterative function over a recursive function:

    pros
    Iteration is faster the recursion,
    Iteration use less menory then recursion,
    cons
    In large program Itration took lots of line of program

"""