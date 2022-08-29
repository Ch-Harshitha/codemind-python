n=int(input())
a=list(map(int,input().split()))
os=0
es=0
for i in range(n):
    if(i%2==0):
        es+=a[i]
    else:
        os+=a[i]
d=os-es
if(d==0):
    print('YES')
else:
    print('NO')