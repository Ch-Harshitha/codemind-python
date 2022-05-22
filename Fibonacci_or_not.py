N=int(input())
if N==0 or N==1:
    print('True')
else:    
    a=0
    b=1
    c=a+b
    while(c<N):
        a=b
        b=c
        c=a+b
    if c==N:
        print('True')
    else:
        print('False')