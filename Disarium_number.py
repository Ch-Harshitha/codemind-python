def count(n):
    l=0
    while(n!=0):
        l+=1
        n//=10
    return l
t=int(input())
n=t
len=count(n)
sum=0
while(n!=0):
    r=n%10
    sum=sum+r**len
    n//=10
    len-=1
if(t==sum):
    print('True')
else:
    print('False')