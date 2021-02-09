h=109
a,b=map(int,input().split())
q=int(a*b)
if q>0:
    d=int(h-q)
else:
    q*=-1
    d=int(h-q)
if d<0:
    print(d*(-1))
else:
    print (d) 