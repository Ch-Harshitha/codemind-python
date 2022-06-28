n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
s=0
s1=0
for i in range(n):
    s1=s1+a[i]
    if a[i]>=x and a[i]<=y:
        s=s+a[i]
print(s1-s)
        