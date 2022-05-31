n=int(input())
for i in range(1,n):
    if(n==i*i+1):
        print('NO')
        break
else:
    print('YES')