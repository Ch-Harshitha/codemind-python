def isprime(j):
    i=2
    v=0
    while i!=j:
        if j%i==0:
            v=1
        i+=1
    if v==0:
        return j
x=int(input())
for i in range(x):
    y=int(input())
    a=y
    for j in range(y,2-1,-1):
        if isprime(j):
            n=j
            break
    while a!=0:
        if isprime(a):
            m=a
            break
        a+=1
    if(y-n)<(m-y):
        print(n)
    elif(y-n)==(m-y):
        print(n)
    else:
        print(m)