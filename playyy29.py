u,k=map(int,input().split())
c=1
for i in range(u,k+1):
  o=i
  g=o**2
  if g==i:
    c=c+1
print(c)
