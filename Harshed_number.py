def harsh(n):
    sum=0
    while(n!=0):
        r=n%10
        sum=sum+r
        n//=10
    return sum
n=int(input())
if n%harsh(n)==0:
    print('True')
else:
    print('False')