n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    if a[i]==1 or a[i]==0:
        s+=1
if s==n:
    print('True')
else:
    print('False')