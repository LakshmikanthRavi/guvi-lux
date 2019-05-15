s=int(input())
h1=int(input())
s1=list(str(h1))
li=[]
l=[]
for i in range(0,s-1):
    if s1[i]>=s1[i+1]:
        li.append(s1[i])
for i in li:
    if int(i)>0:
        l.append(i)
print(*l)

