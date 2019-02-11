a,b=map(int,input().split())
c=list(map(int,input().split()))
z=0
for i in c:
  if i==b:
    z=z+1
for i in range (z):  
  c.remove(b)
print(*c)
    
