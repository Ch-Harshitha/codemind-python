n=input()
x=[]
for i in n:
    if i.isdigit():
        x.append(int(i))
print(sum(x))        