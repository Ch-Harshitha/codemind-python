s=input()
v='aeiouAEIOU'
c=0
for i in s:
    if i in v:
        c+=1
print(c)