a=int(input())
b=int(input())
for i in range(0,b):
    w,h=map(int,input().split())
    if w<a or h<a:
        print('UPLOAD ANOTHER')
    elif w==h:
        print('ACCEPTED')
    elif w==a and h==a:
        print('ACCEPTED')
    elif w>a or h>a:
        print('CROP IT')