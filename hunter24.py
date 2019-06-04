k,l=map(int,input().split())
g=list(map(int,input().split()))
fact=1
c=[]
for i in range(0,k-1):
    for j in range(i+1,k):
        if g[i]+g[j]==l:
            c=1
            break
if c==1:
    print("YES")
else:
    print("NO")
