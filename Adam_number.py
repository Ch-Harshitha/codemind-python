def rev(n):
    rem=0
    while(n!=0):
        r=n%10
        rem=rem*10+r
        n//=10
    return rem
n=int(input())
s=n*n
n1=rev(n)
s1=n1*n1
if(rev(s1)==s):
    print('True')
else:
    print('False')