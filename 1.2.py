a=int(input())
b=int(input())
m=int(input())
print((a*b)%m)
n=0
c=b
while c>0:
    n+=1
    c//=2
c=b
b2=[]
for i in range (n-1,-1,-1):
    b2.append(c%2)
    c//=2
#for i in range (0,n):
    #print (b2[i])
    
P=a*b2[n-1]*2+a*b2[n-2]
for i in range (n-2,0,-1):
    f=P
    P=a*b2[i-1]+2*f
#print(P)
print (P%m)
x=int(input())
y=int(input())
print((x+y)%m)
print(((x%m)+(y%m))%m)
    
    
