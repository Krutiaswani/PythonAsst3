def factorial(n):
    if n==1:
        fac=1
        return fac
    else:
        fac=n*factorial(n-1)
        return fac

n=int(input("Enter a number "))
print(f"Factorial of number {n} is : {factorial(n)}")