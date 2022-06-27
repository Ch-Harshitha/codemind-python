s=input()
v='aeiouAEIOU'
c=0
for i in sorted(set(s),key=s.index):
    if i in v:
        print(i,end=' ')
        c+=1
if c==0:
    print('-1')