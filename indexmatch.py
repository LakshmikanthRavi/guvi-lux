y=int(input())
u=list(map(int,input().split()))
li=[]
for i,j in enumerate(u):
  if(i==j):
    li.append(i)
li.sort()
print(*li)
