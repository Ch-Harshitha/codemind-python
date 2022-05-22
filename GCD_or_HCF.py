n,m=map(int,input().split())
for i in range(1,n+1 and m+1,1):
    if n%i==0 and m%i==0:
        gcd=i
print(gcd)        