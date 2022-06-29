n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in range(n):
    s=s+a[i]
avg=s/n
for j in range(n):
    if a[j]<=avg:
        c+=1
print(c)