a=int(input())
c=list(map(str,input().split()))
z=int(input())
v=len(str(z))
s=0
for i in c:
  d=i[:v+1]
  if int(d)==z:
    s=s+1
print(s)
  
    
