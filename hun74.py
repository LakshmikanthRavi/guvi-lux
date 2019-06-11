s=input()
g=input()
l=[]
li=[]
p=[]
o=[]
z=[]
q=[]
for i in range(0,len(s)):
    for j in range(0,len(s)+1):
        l.append(s[i:j])
for i in range(0,len(g)):
    for j in range(0,len(g)+1):
        li.append(g[i:j])
for i in l:
    for j in li:
        if i==j:
            p.append(i)
for i in p:
    if i != '':
        o.append(i)
for i in o:
    z.append(len(i))
v=max(z)
for i in o:
    if len(i)==v:
        q.append(i)
print(max(q))
