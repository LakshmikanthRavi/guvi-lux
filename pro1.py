n=int(input())
l=[]
p=[]
o=[]
u=[]
c=0
for i in range(0,n):
    h=input()
    l.append(h)
for i in l:
    for j in range(0,len(i)+1):
        p.append(i[:j])
for i in p:
    if i!='':
        u.append(i)
for i in u:
    o.append(p.count(i))
for i in range(0,len(o)):
    c=c+1
    if o[i]!=n:
        break
print(u[c-2])
        
    


