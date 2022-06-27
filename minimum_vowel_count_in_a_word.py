s=input()
x=s.split()
I=[]
for i in x:
    v=sum(letter in 'aeiou' for letter in i.lower())
    I.append(v)
print(min(I))