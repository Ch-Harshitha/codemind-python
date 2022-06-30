t=int(input())
for i in range(t):
    n,m=list(map(int,input().split()))
    c=0
    for j in range(n,m+1):
        d=j%10
        if(d==2 or d==3 or d==9):
            c+=1
    print(c)