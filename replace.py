u=input()
r=len(str(u))
o=r//2
p=u[o:o+1]
c=u[o-1:o]
if r%2!=0:
  y=u.replace(p,"*")
  print(y)
else:
  f=u.replace(c,"*")
  g=f.replace(p,"*")
  print(g)
