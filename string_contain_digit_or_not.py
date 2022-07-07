x=input()
v=[]
for i in x:
    if i.isdigit():
        v.append(i)
p=(len(v))
if p==0:
    print("Doesn't contain digit")
else:
    print("Contains %d digit" %p)