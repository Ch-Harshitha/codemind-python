m,n=map(int,input().split())
for i in range(1,m and n):
    if m%i==0 and n%i==0:
        gcd=i
lcm=(m*n)/gcd
print("%d"%lcm)