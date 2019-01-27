u,m=map(int,input().split())
g=m*u
for i in range(0,g+1):
  y=i**2
  if(g==y):
    print("yes")
    break
else:
  print("no")
