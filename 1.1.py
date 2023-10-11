n=int(input())
x0=int(input())
a=[]
for i in range(0,n+1):
    a.append(int(input()))
P=0
for i in range (n,-1,-1):
    P+=a[i]*(x0**i)
print(P)
p=0
for i in range (n,-1,-1):
    p+=(i-1)*a[i]*(x0**(i-1))
    print(i,p)
print(p)
P=a[n-1]+a[n]*x0
for i in range (n-1,0,-1):
    f=P
    P=a[i-1]+x0*f
print (P)

