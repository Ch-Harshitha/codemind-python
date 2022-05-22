def count(n):
    c=0
    while(n!=0):
        c+=1
        n=n//10
    return c
def first(n,x):
    len=count(n)
    while(len>x):
        n=n//10
        len-=1
    first=n
    return first
def last(n,x):
    i=0
    m=1
    while(i<x):
        m=m*10
        i+=1
    last=n%m
    return last
N,X=map(int,input().split())
print(abs(first(N,X)-last(N,X)))