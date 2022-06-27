def val(re):
    if(re=='I'):
        return 1
    if(re=='V'):
        return 5
    if(re=='X'):
        return 10
    if(re=='L'):
        return 50
    if(re=='C'):
        return 100
    if(re=='D'):
        return 500
    if(re=='M'):
        return 1000
    return -1
def roman(str):
    res=0
    i=0
    while(i<len(str)):
        s1=val(str[i])
        if(i+1<len(str)):
            s2=val(str[i+1])
            if(s1>=s2):
                res=res+s1
                i=i+1
            else:
                res=res+s2-s1
                i=i+2
        else:
            res=res+s1
            i=i+1
    return res
n=input()
print(roman(n))
            
        