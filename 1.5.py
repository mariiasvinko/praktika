def factorial (n):
    f=1
    for i in range (2,n+1):
        f*=i
    return (f)
def factorial_zeros (n):
    return (n//5)
n=int(input())
print(factorial(n))
print(factorial_zeros(n))
