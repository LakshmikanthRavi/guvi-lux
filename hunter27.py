u=input()
li=[]
l=[]
k=[]
a=[]
o=[]
p=[]
for i in range(0,len(u)+1):
    for j in range(0,len(u)+1):
        li.append(u[i:j])
for i in li:
    if i!='':
        l.append(i)
for i in l:
    r="".join(reversed(i))
    a.append(r)
for i in l:
    for j in a:
        if i!=j:
            k.append(i)
for i in k:
    o.append(len(i))
t=max(o)
for i,j in enumerate(o):
    if j==t:
        p.append(k[i])
print(p[0])
