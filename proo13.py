g,k=map(int,input().split())
f=list(map(int,input().split()))
li=[]
l=[]
h=[]
for i in range(0,k):
    u,v=map(int,input().split())
    for i in range(u,v+1):
        li.append(f[i-1])
        li.sort()
    l.append(li[0])
    del li[:]
for i in l:
    print(i)
