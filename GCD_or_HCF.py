m,n=map(int,input().split())
for i in range(1,m and n):
    if(n%i==0 and m%i==0):
        gcd=i
print(gcd)