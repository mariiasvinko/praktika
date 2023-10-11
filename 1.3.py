x=int(input())
f=[]
while x>0:
    f2=0
    f0,f1=1,1
    i=0
    while f2<=x:
        f0,f1=f1,f1+f0
        f2=f1
        i+=1
    f.append(i)
    x-=f0
fib=['0']*max(f)
for i in f:
    fib[i-1]='1'
fib=''.join(fib[::-1])
print(fib)
