n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in range(n):
    s=s+a[i]
avg=s//n
for i in range(n):
    if a[i]>=avg:
        c+=1
print(c)