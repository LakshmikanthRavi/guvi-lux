g,h=map(str,input().split())
li=[]
l=[]
for i in g:
  li.append(i)
for i,j in enumerate(li):
  if j==h:
    l.append(i+1)
print(l[0])
