import math
n=int(input())
a=list(map(int,input().split()))
ans=0
x=n-1
for i in range(n):
    ans=ans+(a[i]*pow(2,x))
    x-=1
print(ans)