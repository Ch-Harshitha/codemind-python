t=int(input())
n=t*t
s=0
while(n!=0):
    r=n%10
    s=s+r
    n//=10
if(s==t):
    print('Neon Number')
else:
    print('Not Neon Number')