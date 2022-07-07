n=int(input())
for i in range(n):
    c=int(input())
    s=input()
    for i in range(c):
        if (s.count(s[i])==1):
            print(s[i])
            break
    else:
        print(-1)