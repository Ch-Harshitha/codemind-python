def digit(n):
    while(n):
        r=n%10
        if(r!=2 and r!=3 and r!=5 and r!=7):
            return 0
        n=n//10
    return 1
def prime(n):
    if(n==1):
        return 0
    i=2
    while(i*i<=n):
        if(n%i==0):
            return 0
        i=i+1
    return 1
def isprime(n):
    return (digit(n) and prime(n))
n=int(input())
if (isprime(n)) :
    print("Mega Prime")
else :
    print("Not Mega Prime")