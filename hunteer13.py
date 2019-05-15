t=input()
l=[]
le=[]
li=[]
c=len(t)//2
 
for i in t:
    l.append(i)
for i in range(0,c):
    x=l.pop()
    le.append(x)
for i in range(0,c):
  li.append(l[i])
if le==li:
    print("yes")
else:
    print("no")
