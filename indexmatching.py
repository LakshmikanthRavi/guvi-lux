y=int(input())
u=list(map(int,input().split()))
li=[]
for i,j in enumerate(u):
  if(i==j):
    li.append(i)
if(i!=j):
  print("-1")
else:

  print(*li)
  
