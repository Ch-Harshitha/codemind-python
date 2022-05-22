n=int(input())
s=n*n
l=10**len(str(n))
if(s%l==n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')