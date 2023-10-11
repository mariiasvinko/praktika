a=[]
n=int(input())
for i in range(0,n):
    a.append(int(input()))
k=int(input())
maxs=0
j=0
summ=0
if k>n:
    print("error")
l=n-k+1
h=0
g=k
while h<l:
    for i in range (j,g):
        summ+=a[i]
    if summ>maxs:
        maxs=summ
    h+=1
    j+=1
    g+=1
    summ=0
print(maxs)
        
