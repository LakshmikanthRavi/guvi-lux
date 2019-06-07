f=int(input())
g=list(map(int,input().split()))
g.sort()
li=[]
for i in range(0,f-1):
    if g[i]==g[i+1]:
        li.append(g[i])
for i in g:
    if i not in li:
        print(i)
