n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or j==n or j==1:
            j=''
            print(j,end='* ')
        else:
            print(' ',end=' ')
    print()