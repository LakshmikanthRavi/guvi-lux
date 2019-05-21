v=int(input())
u=list(map(int,input().split()))
li=[]
p=[]
if v%2==0:
    c=1
    f=v//2
else:
    c=0
    g=(v//2)+1
if c==1:
    li.append(u[f:])
    li.append(u[0:f])
    for i in li:
        p.append(sum(i))
    f=p[0]//len(p)
    o=p[1]//len(p)
    if f==o:
        print("yes")
    else:
        print("no")
if c==0:
    li.append(u[:g])
    for i in li:
        x=len(i)
    li.append(u[g:])
    for i in li:
        b=len(i)
    for i in li:
        p.append(sum(i))
    f=p[0]//x
    o=p[1]//b
    if f==o:
        print("yes")
    else:
        print("no")
