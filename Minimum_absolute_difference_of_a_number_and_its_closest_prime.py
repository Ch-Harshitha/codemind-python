def prime(n):
    i=2
    v=0
    while i!=n:
        if(n%i==0):
            v=1
        i+=1
    if(v==0):
        return n
x=int(input())
a=x
for i in range(x,2,-1):
    if prime(i):
        n=i
        break
while a!=0:
    if prime(a):
        m=a
        break
    a+=1
if(x-n)<(m-x):
    print(abs(n-x))
elif(x-n)==(m-x):
    print(abs(n-x))
else:
    print(abs(m-x))