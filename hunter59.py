f=int(input())
g=list(map(int,input().split()))
c=list(map(int,input().split()))
li=[]
for i in range(0,f):
    s=g[i]+c[i]
    li.append(s)
print(*li)
