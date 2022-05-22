def count(n):
    c=0
    while(n!=0):
        c+=1
        n//=10
    return c
def last(n,x):
    i=0
    mod=1
    while(i<x):
        mod=mod*10
        i+=1
    last=n%mod
    return last
def first(n,x):
    length=count(N)
    while(length!=x):
        n//=10
        length-=1
    first=n
    return first
N,X=map(int,input().split())
print(abs(first(N,X)-last(N,X)))