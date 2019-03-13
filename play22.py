v,m=map(int,input().split())
li=[]
for i in range(1,m+1):
  if v%i==0 and m%i==0:
    li.append(i)
if len(li)==1:
  print(*li)
else:
  print(*li[-1:])
