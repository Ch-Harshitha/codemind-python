def reverse(x):
    revstring=''
    for i in x:
        revstring=i+revstring
    print(revstring)
x=str(input())
reverse(x)