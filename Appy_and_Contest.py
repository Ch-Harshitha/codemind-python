x=int(input())
for y in range(x): 
    n,a,b,k,=map(int,input().split())
    l=0
    if a%b==0:
        l=a
    elif b==0:
        l=b
    else:
        l=a*b
        f=n//l
        c=n//a
        d=n//b
        c=c-f
        d=d-f
        if c+d>=k:
            print('Win')
        else:
            print('Lose')