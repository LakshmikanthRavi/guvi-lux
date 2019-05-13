import math
r=int(input())
v=math.radians(r)
c=math.sin(v)
y=round(c,1)
k=abs(y)
if k<1:
  print(y)
else:
print(round(y))
