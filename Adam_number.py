def rev(n):
    re=0
    t=n
    while(t!=0):
        r=t%10
        re=re*10+r
        t//=10
    return re
n1=int(input())
s1=n1*n1
n2=rev(n1)
s2=n2*n2
ms=rev(s2)
if s1==ms:
    print('True')
else:
    print('False')