h=int(input())
g=list(map(int,input().split()))
l=[]
o=min(g)
k=max(g)
for i,j in enumerate(g):
    if j==o:
        l.append(i+1)
for i,j  in enumerate(g):
    if j==k:
        l.append(i+1)
print(*l)
