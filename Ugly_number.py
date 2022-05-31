def ugly(n):
    if(n==1):
        return True
    if(n<=0):
        return False
    if(n%2==0):
        return (ugly(n=n//2))
    if(n%3==0):
        return (ugly(n=n//3))
    if(n%7==0):
        return (ugly(n=n//7))
n=int(input())
if(ugly(n)):
    print('Ugly Number')
else:
    print('Not Ugly Number')