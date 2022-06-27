def prime(n):
    if(n==1):
        return 0
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
n=int(input())
z=0
for i in range(2,n):
    if n%i==0:
        if(prime(i)):
            print(i,end=' ')
            z+=1
if(z==0):
    print('-1')