def palindrome(n):
    re=0
    while(n!=0):
        r=n%10
        re=re*10+r
        n//=10
    return re
T=int(input())
for i in range(1,T+1):
    n=int(input())
    if n==palindrome(n):
        print('True')
    else:
        print('False')