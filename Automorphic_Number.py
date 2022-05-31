def count(n):
    c=0
    while(n!=0):
        c+=1
        n//=10
    return c
n=int(input())
s=n*n
p=s%(10**count(n))
if(p==n):
    print('Automorphic Number');
else:
    print('Not an Automorphic Number')