f=int(input())
g=list(map(int,input().split()))
c=list(map(int,input().split()))
if g[1]!=c[1]:
    l=g[1]
    for i,j in enumerate(g):
        if j==l:
            h=i
    for i,j in enumerate(c):
        if j==l:
            n=i 
    b=abs(h-n)
    print(b)
if g[1]==c[1]: 
    l=g[1]
    for i,j in enumerate(g):
        if j==l:
            h=i
    for i,j in enumerate(c):
        if j==l:
            n=i 
    b=abs(h-n)
    print(b)
    
    


