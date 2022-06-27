s=input()
spe='~!@#$%^&*()_?><{}|/\:,.'
c=0
for i in s:
    if i in spe:
        c+=1
print(c)