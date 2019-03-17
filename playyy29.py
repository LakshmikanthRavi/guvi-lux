u,k=map(int,input().split())
c=0
li=[]
for i in range(1,k+1):
  o=i
  g=o**2
  li.append(g)
for i in range(u,k+1):
  if i in li:
    c=c+1
print(c)

