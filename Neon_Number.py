n=int(input())
sq=n*n
t=sq
sum=0
while(sq!=0):
    r=sq%10
    sum+=r
    sq//=10
if n==sum:
    print('Neon Number')
else:
    print('Not Neon Number')