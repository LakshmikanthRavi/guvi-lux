h=int(input())
l=list(map(str,input().split()))
li=[]
r=l[1:]
y=min(l)
if y==l[0]:
    for i in range(0,len(l)):
        x=l.pop(0)
        if y<=x:
            li.append(y)
else:
    li.append(l[0])
    for i in range(0,len(l)-1):
        x=l.pop(0)
        
        if r[i]<x:
            li.append(r[i])
        else:
            li.append(x)
print(*li)

    
        
        
