h,k=map(str,input().split())
p=int(k)
li=[]
l=[]
for i in range(0,len(h)+1):
    for j in range(0,len(h)+1):
        li.append(h[i:j])
for i in li:
    if len(i)==p:
        l.append(i)
print(*l)
