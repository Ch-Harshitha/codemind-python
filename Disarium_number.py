def count(n):
    c=0
    while(n!=0):
        n//=10
        c+=1
    return c
n=int(input())
sum=0
t=n
c=count(n)
while(t!=0):
    r=t%10
    sum=sum+r**c
    t//=10
    c-=1
if(sum==n):
    print('True')
else:
    print('False')