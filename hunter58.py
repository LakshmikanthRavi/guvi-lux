f,k=map(int,input().split())
g=list(map(int,input().split()))
c=0
for i in range(0,f):
    for j in range(0,f):
        if g[i]-g[j]==k:
            c=c+1 
print(c)
