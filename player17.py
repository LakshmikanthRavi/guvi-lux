u,v=map(int,input().split())
li=[]
l=[]
y=[]
k=v*v
for i in range(0,k):
  n=u*i
  li.append(n)
  m=v*i
  l.append(m)
for i in li:
  for j in l:
    if i==j:
      y.append(i)
print(y[1])
