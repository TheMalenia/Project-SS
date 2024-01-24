import math
#make a random number between 0 and 1
def rand01(mult=2**15-19,mod=2**31-1,base=2**10,cst=1,size=1000):
    s=[0]*size
    x=(base*mult+cst)%mod
    s[0]=x/mod
    i=1
    while i<size:
        x=(x*mult+cst)%mod
        s[i]=x/mod
        i+=1
    return s
#make a random number between a and b
def random(a,b,base=2**10,size=1):
    s=rand01(base=base,size=size)
    i=0
    while i<len(s):
        if s[i]==1:
            s[i]=0
        s[i]=a+(b-a)*s[i]
        i+=1
    return s
