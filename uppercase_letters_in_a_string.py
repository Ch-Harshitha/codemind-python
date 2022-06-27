s=input()
I='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c=0
for i in s:
    if i in I:
        c+=1
print(c)