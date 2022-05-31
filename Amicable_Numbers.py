m=int(input())
n=int(input())
s1=0
for i in range(1,m):
    if(m%i==0):
        s1+=i
s2=0
for i in range(1,n):
    if(n%i==0):
        s2+=i
if(s1==n and s2==m):
    print('Amicable')
else:
    print('Not Amicable')
