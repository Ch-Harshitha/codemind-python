def prime(n):
    c=0
    for i in range(2,n//2):
        if n%i==0:
            c+=1
    if c==0:
        return 1
    else:
        return 0
n=int(input())
rev=0
temp=n
while(temp!=0):
    rev=rev*10+temp%10
    temp=temp//10
if(prime(n) and prime(rev)):
    print('circular prime')
elif(prime(n) or prime(rev)):
    print('prime but not a circular prime')
else:
    print('not prime')