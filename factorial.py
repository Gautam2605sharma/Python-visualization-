def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
n=int(input("enter the number= "))
print("factorial of given number is ",fact(n))