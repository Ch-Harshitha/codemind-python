n=int(input())
l=[]
a=list(map(int,input().split()))
for i in range(n):
    a[i]=a[i]*a[i]
    l.append(a[i])
print(*sorted(l))