def dig(n):
    if n==0:
        return 1
    s=0
    if n<0:
        n=-1*n
    while n!=0:
        i=n%10
        n=n//10
        s+=1
    return s
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    print(dig(a[i]),end=' ')