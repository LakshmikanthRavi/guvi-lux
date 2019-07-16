n=int(input())
l=list(map(int,input().split()))
p=[]
t=[]
u=[]
o=[]
for i in range(0,len(l)+1):
    for j in range(0,len(l)+1):
        p.append(l[i:j])
for i in p:
    if i!=[]:
        t.append(i)
for i in t:
    if sorted(i)==i:
        u.append(i)
for i in u:
    o.append(len(i))
print(max(o))

