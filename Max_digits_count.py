def dig(n):
    if n==0:
        return 1
    s=0
    while n!=0:
        i=n%10
        n=n//10
        s+=1
    return s
n=int(input())
a=list(map(int,input().split()))
I=[]
for i in range(n):
    I.append(dig(a[i]))
k=max(I)
print(I.count(k))
