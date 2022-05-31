def large(n):
    l=0
    while(n!=0):
        r=n%10
        if(r>l):
            l=r
        n//=10
    return l
n=int(input())
print(large(n))