a=int(input())
arr=list(map(int,input().strip().split()))[:a]
c=0
oc=0
ec=0
for i in range(a):
    if (arr[i]%2):
        oc+=1
    else:
        ec+=1
print(ec,oc)        