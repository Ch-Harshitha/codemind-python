s=list(map(str,input().split()))
I=[]
for i in s:
    c=0
    for j in i:
        c+=1
    I.append(c)
    c=0
print(max(I))