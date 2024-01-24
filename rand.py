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
