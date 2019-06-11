u=int(input())
g=list(map(int,input().split()))
l=[]
for i in range(0,len(g)-1):
    if g[i]>g[i+1]:
        l.append(g[i+1])
    else:
        l.append(-1)
l.append(-1)
print(*l)
