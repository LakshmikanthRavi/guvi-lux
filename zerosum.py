f=int(input())
p=list(map(int,input().split()))
for i in p:
  for j in p:
    y=i+j
    if y==0:
      l=i
      u=j
print(l,u) 
